from prop_logic import AtomConnected
from hex_diagram import *
from lemma import LemmaDatabase
import pickle

class BuildSplit:
    def __init__(self, goal, pos, first_connect_up):
        self.waiting_for_thm = True
        self.main = goal
        self.pos = pos
        self.node = int(self.main.pos_to_node[pos])
        assert self.node in self.main.red_nodes
        assert self.node not in (self.main.up_node, self.main.down_node)

        self.first_connect_up = first_connect_up
        self._thm_up = None
        self._thm_down = None
        self._build_current_goal(first_connect_up)

    @property
    def phase(self):
        return int(self._thm_up is not None) + int(self._thm_down is not None)

    def use_thm(self):
        thm = self._convert_theorem()
        if self._current_up:
            self._thm_up = thm
        else:
            self._thm_down = thm
        if self._current_up == self.first_connect_up:
            self._build_current_goal(not self.first_connect_up)
        else:
            self._finish()

    def _build_current_goal(self, connect_up):
        self._current_up = connect_up

        kwargs = dict(self.main.kwargs)
        thm = None
        if self._thm_up is not None: thm = self._thm_up
        if self._thm_down is not None: thm = self._thm_down
        if thm is not None:
            used = thm.strategy.nodes
            node_mask_1d = np.array([
                node not in used
                for node in range(self.main.num_nodes)
            ])
            available_mask = self.main.available_mask & node_mask_1d[self.main.pos_to_node]
            kwargs['available_mask'] = available_mask

        if connect_up:
            down_mask = np.array(self.main.down_mask)
            down_mask[self.pos] = True
            kwargs['down_mask'] = down_mask
        else:
            up_mask = np.array(self.main.up_mask)
            up_mask[self.pos] = True
            kwargs['up_mask'] = up_mask

        self.cur = HexDiagram(**kwargs)

    def _convert_theorem(self):
        homo = self.cur.align_map(identity_transform, self.main)
        homo[self.cur.up_node] = self.main.up_node
        homo[self.cur.down_node] = self.main.down_node
        thm = self.cur.thm.map_nodes(homo)
        if self._current_up: main_node = self.main.down_node
        else: main_node = self.main.up_node
        neighbors = set()

        for a,b in self.main.edges:
            if a == self.node: neighbors.add(b)
            elif b == self.node: neighbors.add(a)
        for a,b in self.main.edges:
            if a == main_node: neighbors.discard(b)
            elif b == main_node: neighbors.discard(a)

        thm = thm.split_node(main_node, self.node, neighbors)
        return thm

    def _finish(self):
        self.cur = None

        thm = core.transitivity(self.main.up_node, self.node, self.main.down_node)
        thm = thm & self._thm_up & self._thm_down
        self.main.add_theorem(thm)

        self.cur = None
        self.waiting_for_thm = False

class InternalConnection:
    def __init__(self, goal, pos1, pos2):
        self.waiting_for_thm = True
        self.main = goal
        self.pos1 = pos1
        self.pos2 = pos2
        # currently relies on the border nodes being red,
        # could be more general but requires more careful handling of the theorems
        assert self.main.red_mask[pos1] and self.main.red_mask[pos2]
        self.node1 = int(self.main.pos_to_node[pos1])
        self.node2 = int(self.main.pos_to_node[pos2])
        assert self.node1 != self.node2
        assert frozenset((self.node1, self.node2)) not in goal.edges
        nodes = (self.node1, self.node2)
        assert self.main.up_node not in nodes or self.main.down_node not in nodes

        self._internal_thm = None
        self._external_thm = None
        self._build_internal_goal()

    def use_thm(self):
        if self._internal_thm is None:
            thm = self.cur.thm
            homo = self.cur.align_map(identity_transform, self.main)
            self._internal_thm = thm.map_nodes(homo)
            self._build_external_goal()
        else:
            # split the red node into transitivity
            self._extract_external_thm()
            self.cur = None
            [final_connection] = self._internal_thm.clause.corollaries
            if final_connection in self._external_thm.clause.assumptions:
                self.main.add_theorem(self._external_thm & self._internal_thm)
            else:
                self.main.add_theorem(self._external_thm)

    def _build_internal_goal(self):
        kwargs = dict(self.main.kwargs)
        kwargs['up_edge'] = False
        kwargs['down_edge'] = False
        up_mask = np.zeros(self.main.shape, dtype = bool)
        up_mask[self.pos1] = True
        down_mask = np.zeros(self.main.shape, dtype = bool)
        down_mask[self.pos2] = True
        kwargs['up_mask'] = up_mask
        kwargs['down_mask'] = down_mask
        kwargs['red_mask'] = self.main.up_mask | self.main.down_mask | self.main.red_mask
        self.cur = HexDiagram(**kwargs)
    def _build_external_goal(self):
        kwargs = dict(self.main.kwargs)

        # erase used nodes
        used = self._internal_thm.strategy.nodes
        node_mask_1d = np.array([
            node not in used
            for node in range(self.main.num_nodes)
        ])
        available_mask = self.main.available_mask & node_mask_1d[self.main.pos_to_node]
        kwargs['available_mask'] = available_mask

        # add connection
        extra_edges = self.main.extra_edges + ((self.pos1, self.pos2),)
        kwargs['extra_edges'] = extra_edges

        self.cur = HexDiagram(**kwargs)

    def _extract_external_thm(self):
        thm = self.cur.thm
        homo = self.cur.align_map(identity_transform, self.main)
        node1, node2 = self.node1, self.node2
        node_cur = int(self.cur.pos_to_node[self.pos1])
        adjs1 = []
        adjs2 = []
        for atom in thm.clause.assumptions:
            if isinstance(atom, AtomConnected) and node_cur in atom.nodes:
                adj_cur = atom.other_node(node_cur)
                adj = homo[adj_cur]
                edge1 = frozenset((node1, adj)) in self.main.edges
                edge2 = frozenset((node2, adj)) in self.main.edges
                if edge1 and not edge2: adjs1.append(adj)
                if edge2 and not edge1: adjs2.append(adj)
        if len(adjs2) > len(adjs1):
            node1,node2 = node2,node1
            adjs1,adjs2 = adjs2,adjs1

        # relabel nodes
        homo[node_cur] = node1
        thm = thm.map_nodes(homo)

        # split using transitivity
        for adj in adjs2:
            thm = thm & core.transitivity(node1, node2, adj)

        self._external_thm = thm

class BuildCases:
    def __init__(self, goal):
        self.main = goal
        self._tried_moves = []
        self._remaining_blue = None
        self._cur_blue = None
        self._cur_red = None
        self.waiting_for_thm = False

    def use_thm(self):
        assert self.waiting_for_thm
        self._use_thm(self._convert_theorem())

    def _use_thm(self, thm):
        nodes = set(thm.strategy.nodes)
        nodes.add(self._cur_red)
        if self._remaining_blue is None:
            self._remaining_blue = nodes
        else:
            self._remaining_blue &= nodes
        if self._remaining_blue:
            self._cur_blue = min(self._remaining_blue)
        else:
            self._cur_blue = None

        self._tried_moves.extend([self._cur_red, thm])

        self._cur_red = None
        self.waiting_for_thm = False
        if self._remaining_blue: self._build_current_goal()
        else: self._finish()

    def make_red_move(self, pos):
        assert not self.waiting_for_thm
        assert self.main.empty_mask[pos]
        node = int(self.main.pos_to_node[pos])
        assert node != self._cur_blue
        self._cur_red = node
        self.waiting_for_thm = True
        thm = self._get_finishing_thm()
        if thm is None: self._build_current_goal()
        else: self._use_thm(thm)

    def make_blue_move(self, pos):
        assert not self.waiting_for_thm
        assert self.main.empty_mask[pos]
        node = int(self.main.pos_to_node[pos])
        if self._remaining_blue:
            assert node in self._remaining_blue
        self._cur_blue = node
        self._build_current_goal()

    def remove_move(self):
        assert self.waiting_for_thm
        self.waiting_for_thm = False
        self._cur_red = None
        self._build_current_goal()

    def _build_current_goal(self):
        assert self._cur_red not in self.main.red_nodes

        kwargs = dict(self.main.kwargs)
        if self._cur_red is not None:
            [pos] = self.main.components[self._cur_red]
            red_mask = np.array(self.main.red_mask)
            red_mask[pos] = True
            kwargs['red_mask'] = red_mask
        if self._cur_blue is not None:
            [pos] = self.main.components[self._cur_blue]
            available_mask = np.array(self.main.available_mask)
            available_mask[pos] = False
            kwargs['available_mask'] = available_mask
        self.cur = HexDiagram(**kwargs)

    def _get_finishing_thm(self):
        edge_up = frozenset((self.main.up_node, self._cur_red))
        edge_down = frozenset((self.main.down_node, self._cur_red))
        if edge_up in self.main.edges and edge_down in self.main.edges:
            return core.transitivity(
                self.main.up_node,
                self._cur_red,
                self.main.down_node,
            )
        else:
            return None

    def _convert_theorem(self):
        alignment = self.cur.align_with(identity_transform, self.main)
        glued_i,glued = next(
            (comp_i,comp)
            for comp_i,comp in alignment.items()
            if self._cur_red in comp
        )
        homo = {
            i : next(iter(comp))
            for i,comp in alignment.items()
            if self._cur_red not in comp
        }

        transitivities = []
        # resolve node gluing with transitivity
        if len(glued) == 1: homo[glued_i] = next(iter(glued))
        else:
            glued_to_neighbors = { n : set() for n in glued }
            for (a,b) in self.main.edges:
                if a in glued: glued_to_neighbors[a].add(b)
                if b in glued: glued_to_neighbors[b].add(a)
            if self.main.up_node in glued:
                glued_main = self.main.up_node
            elif self.main.down_node in glued:
                glued_main = self.main.down_node
            else:
                glued_main = max(
                    glued - set([self._cur_red]),
                    key = lambda n: len(glued_to_neighbors[n])
                )

            homo[glued_i] = glued_main
            glued_rest = glued - set([self._cur_red, glued_main])
            for node in glued_rest:
                transitivities.append(core.transitivity(glued_main, self._cur_red, node))
            glued_rest.add(self._cur_red)
            for a in glued_rest:
                for b in glued_to_neighbors[a]:
                    transitivities.append(core.transitivity(glued_main, a, b))
            transitivities.reverse()

        thm = self.cur.thm.map_nodes(homo)
        for trans in transitivities:
            [atom] = trans.clause.corollaries
            if atom in thm.clause.assumptions:
                thm = thm & trans

        return thm

    def _finish(self):
        thm = core.build_case_strategy(*self._tried_moves)
        self.main.add_theorem(thm)
        self.cur = None

class GoalEnv:
    def __init__(self, goal_diagram, finished_trigger = None):
        self.steps = []
        self.main = goal_diagram
        self.fork = core.build_case_strategy(
            1, core.transitivity(0,1,3),
            2, core.transitivity(0,2,3),
        )
        self.initialize()
        self.finished_trigger = finished_trigger

    def initialize(self):
        self.cur = self.main
        self.stack = []
        self.lemma_database = LemmaDatabase(self.main)
        self.finished = False

    @property
    def waiting_for_thm(self):
        if self.finished: return False
        if not self.stack: return True
        return self.stack[-1].waiting_for_thm
    @property
    def last(self):
        if not self.stack: return None
        else: return self.stack[-1]

    def to_pos(self, pos_or_node):
        if isinstance(pos_or_node, int):
            return self.cur.components[pos_or_node][0]
        else:
            return pos_or_node

    def split_node(self, pos, first_connect_up = True):
        pos = self.to_pos(pos)
        assert self.waiting_for_thm
        self.stack.append(BuildSplit(self.cur, pos, first_connect_up))
        self.steps.append(("split_node", pos, first_connect_up))
        self._finish()
        return True

    def internal_connection(self, pos1, pos2):
        pos1 = self.to_pos(pos1)
        pos2 = self.to_pos(pos2)
        assert self.waiting_for_thm
        self.stack.append(InternalConnection(self.cur, pos1, pos2))
        self.steps.append(("internal_connection", pos1, pos2))
        self._finish()
        return True

    def _get_cases_builder(self):
        if self.waiting_for_thm:
            cases_builder = BuildCases(self.cur)
            self.stack.append(cases_builder)
        else:
            cases_builder = self.stack[-1]
            assert isinstance(cases_builder, BuildCases)
        return cases_builder

    def make_red_move(self, pos):
        pos = self.to_pos(pos)
        assert not self.finished
        assert self.main.empty_mask[pos]
        self._get_cases_builder().make_red_move(pos)
        self.steps.append(("make_red_move", pos))
        self._finish()
        return True

    def make_blue_move(self, pos):
        pos = self.to_pos(pos)
        assert not self.finished
        self._get_cases_builder().make_blue_move(pos)
        self.steps.append(("make_blue_move", pos))
        self._finish()
        return True

    def close_with_proven(self, proven_diagram, transform):
        assert self.waiting_for_thm

        # glue if necessary
        homo = proven_diagram.align_map(transform, self.cur)
        thm = proven_diagram.thm.map_nodes(homo, conflict_to_red = True)
        thm = thm.remove_reflexivity_assumptions()

        self.cur.add_theorem(thm)
        self._finish()
        return True

    def close_with_lemma(self, include_red):
        if not self.waiting_for_thm:
            return False
        thm = self.lemma_database.find(self.cur, include_red = include_red)
        if thm is not None:
            self.cur.add_theorem(thm)
            self.steps.append(("close_with_lemma", include_red))
            self._finish(save_first = False)
            return True
        else:
            return False

    def close_with_fork(self):
        if self.finished: return False
        up_node = self.cur.up_node
        down_node = self.cur.down_node
        nodes = []
        for node in self.cur.empty_nodes:
            if frozenset((node, up_node)) not in self.cur.edges: continue
            if frozenset((node, down_node)) not in self.cur.edges: continue
            [pos] = self.cur.components[node]

            # prefer forks that appeared recently
            penalty = 0
            for builder in self.stack:
                if builder.main.available_mask[pos]:
                    local_node = builder.main.pos_to_node[pos]
                    local_edge0 = frozenset((local_node, builder.main.up_node))
                    local_edge1 = frozenset((local_node, builder.main.down_node))
                    local_edges = builder.main.edges
                    if local_edge0 in local_edges and local_edge1 in local_edges:
                        penalty += 1
            nodes.append((penalty, node))

        nodes.sort()
        nodes = [node for score, node in nodes]
        if self.waiting_for_thm:
            if len(nodes) < 2: return False
            node1, node2 = nodes[:2]
            self.cur.add_theorem(self.fork.map_nodes([
                up_node, node1, node2, down_node
            ]))
            self.steps.append(("close_with_fork",))
            self._finish(save_first = False)
            return True

        else:
            assert isinstance(self.last, BuildCases)
            for node in nodes:
                [pos] = self.cur.components[node]
                if self.last._remaining_blue is not None and self.last.main.pos_to_node[pos] not in self.last._remaining_blue:
                    self.last.make_red_move(pos)
                    self._finish()
                    return True
            return False

    def pop_stack(self):
        if not self.stack: return False
        self.steps.append(("pop_stack", ))
        last = self.stack[-1]
        if isinstance(last, BuildCases) and last.waiting_for_thm:
            if last._tried_moves:
                last.remove_move()
                self._finish()
                return True

        self.stack.pop()
        self._finish()
        return True

    def _finish(self, save_first = True):
        if self.finished: return
        while self.stack:
            if self.stack[-1].cur is not None and self.stack[-1].cur.thm is not None:
                if save_first:
                    self.lemma_database.add(self.stack[-1].cur)
                save_first = True
                self.stack[-1].use_thm()
            if self.stack[-1].cur is None:
                self.stack.pop()
            else:
                break

        if self.stack: self.cur = self.stack[-1].cur
        elif self.main.thm is None: self.cur = self.main
        else:
            self.finished = True
            self.cur = None
            if self.finished_trigger is not None:
                self.finished_trigger()

    def save_steps(self, fname):
        with open(fname, 'wb') as f:
            pickle.dump(self.steps, f)

    def load_steps(self, fname):
        with open(fname, 'rb') as f:
            steps = pickle.load(f)
        self.initialize()
        for i,(f,*args) in enumerate(steps):
            # print(f, args)
            try:
                f = getattr(self, f)
                assert f(*args)
            except:
                print(f"Warning: Reconstruction failed, only {i} / {len(steps)} steps were recovered")
                break

if __name__ == "__main__":
    from save_proof import export_proof_to_file

    def make_board(size, move0):
        red_mask = np.zeros([size,size], dtype = bool)
        red_mask[move0] = True
        return HexDiagram(
            available_mask = np.ones([size,size], dtype = bool),
            red_mask = red_mask,
            up_mask = np.zeros([size,size], dtype = bool),
            down_mask = np.zeros([size,size], dtype = bool),
            up_edge = True,
            down_edge = True,
        )

    board6 = make_board(6,(2,3))

    diagrams = HexDiagram.parse_file("hexwiki_templates.hdg")
    diagram = diagrams[35]
    env = GoalEnv(diagram)
    env.load_steps("proofs/hexwiki_templates_36_steps.pkl")
    # env.make_red_move((2,8))

    if env.finished:
        print("Problem solved!")
        print(env.main)
    else:
        print(env.cur.to_str('enum'))

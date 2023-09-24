from hex_diagram import identity_transform
from prop_logic import AtomConnected
from collections import defaultdict
import numpy as np

from logic_core import Proof

def collect_proof_history(proof, res = None):
    if res is None: res = set()
    if proof in res: return res
    res.add(proof)
    for arg in proof.args:
        if isinstance(arg, Proof):
            collect_proof_history(arg, res)
    return res

class Lemma:
    def __init__(self, main, cur, is_goal = False, include_red = False):
        self.main = main
        self.cur = cur
        self.is_goal = is_goal

        if not self.is_goal: assert cur.thm is not None

        alignment = self.cur.align_with(identity_transform, main)
        self.alignment = alignment

        main_empty_mask = np.array([
            (node in main.empty_nodes)
            for node in range(main.num_nodes)
        ], dtype = bool)

        if is_goal:
            used_nodes = cur.empty_nodes
            clause = cur.clause
        else:
            used_nodes = cur.thm.strategy.nodes
            clause = cur.thm.clause

        self.used = np.zeros(main.num_nodes, dtype = bool)
        self.used_idx = np.zeros(main.num_nodes, dtype = int)
        for local_node in used_nodes:
            [node] = alignment[local_node]
            self.used[node] = True
            self.used_idx[node] = local_node

        # calculate empty nodes adjacent to red nodes
        red_node_to_adj = defaultdict(lambda: np.zeros(main.num_nodes, dtype = bool))
        for assump in clause.assumptions:
            if isinstance(assump, AtomConnected):
                [a,b] = assump.nodes
                if a not in used_nodes:
                    a,b = b,a
                elif b in used_nodes: continue
                assert a in used_nodes
                [main_a] = alignment[a]
                red_node_to_adj[b][main_a] = True

        if include_red:
            # add self-loops to red nodes & add them to used
            # to make possible to use the lemma even when there are more red nodes
            for local_node in cur.red_nodes:
                nodes = alignment[local_node]
                adj = red_node_to_adj[local_node]
                for node in nodes:
                    self.used[node] = True
                    adj[node] = True
                    self.used_idx[node] = local_node

        red_node_to_adj[self.cur.up_node] # assure existence
        red_node_to_adj[self.cur.down_node]

        # truncate masks to only empty nodes
        self.used = self.used[main_empty_mask]
        red_node_to_adj = {
            key : value[main_empty_mask]
            for key, value in red_node_to_adj.items()
        }
        self.used_idx = self.used_idx[main_empty_mask]

        self.up_idx = self.cur.up_node
        self.down_idx = self.cur.down_node
        self.up_adj = red_node_to_adj[self.up_idx]
        self.down_adj = red_node_to_adj[self.down_idx]

        red_nodes_sorted = list(red_node_to_adj.items())
        edge_nodes = (self.up_idx, self.down_idx)
        red_nodes_sorted.sort(
            key = lambda kv: (kv[0] not in edge_nodes, -np.sum(kv[1]))
        )
        red_nodes_filtered = []
        for red_node, adj in red_node_to_adj.items():
            for prev_nodes, prev_adj in red_nodes_filtered:
                if (adj <= prev_adj).all():
                    prev_nodes.append(red_node)
                    break
            else:
                red_nodes_filtered.append(([red_node], adj))

        self.reds_idx = [
            red_nodes[0] for red_nodes, adj in red_nodes_filtered
        ]
        self.reds_adj = [
            adj for red_nodes, adj in red_nodes_filtered
        ]

        # eliminate extra red nodes from the theorem
        if not self.is_goal:
            self.thm = cur.thm
            homo = dict()
            for red_nodes, adj in red_nodes_filtered:
                node0 = red_nodes[0]
                for node in red_nodes[1:]:
                    homo[node] = node0
            if self.up_idx in homo: del homo[self.up_idx]
            if self.down_idx in homo: del homo[self.down_idx]
            if homo:
                self.thm = self.thm.map_nodes(homo)

    def __hash__(self):
        used = tuple(bool(x) for x in self.used)
        up_adj = tuple(bool(x) for x in self.up_adj)
        down_adj = tuple(bool(x) for x in self.down_adj)
        reds_adj = frozenset(
            tuple(bool(x) for x in red_adj)
            for red_adj in self.reds_adj
        )
        return hash((self.main, used, up_adj, down_adj, reds_adj))

    def __eq__(self, other):
        if not isinstance(other, Lemma): return False
        if self.main != other.main: return False
        if not (self.used == other.used).all(): return False
        if not (self.up_adj == other.up_adj).all(): return False
        if not (self.down_adj == other.down_adj).all(): return False
        reds_adj = frozenset(
            tuple(bool(x) for x in red_adj)
            for red_adj in self.reds_adj
        )
        other_reds_adj = frozenset(
            tuple(bool(x) for x in red_adj)
            for red_adj in other.reds_adj
        )
        if reds_adj != other_reds_adj: return False
        return True

    def get_thm(self, goal):
        if not (self.used <= goal.used).all(): return None
        if not (self.up_adj <= goal.up_adj).all(): return None
        if not (self.down_adj <= goal.down_adj).all(): return None
        for red_adj in self.reds_adj:
            if not any((red_adj <= goal_red_adj).all() for goal_red_adj in goal.reds_adj):
                return None

        # map empty nodes
        homo = dict(zip(
            map(int, self.used_idx[self.used]),
            map(int, goal.used_idx[self.used]),
        ))
        # map red nodes
        for red_idx, red_adj in zip(self.reds_idx, self.reds_adj):
            for goal_red_idx, goal_red_adj in zip(goal.reds_idx, goal.reds_adj):
                if (red_adj <= goal_red_adj).all():
                    homo[red_idx] = goal_red_idx
                    break
        # map endpoints
        homo[self.up_idx] = goal.up_idx
        homo[self.down_idx] = goal.down_idx

        thm = self.thm.map_nodes(homo, conflict_to_red = True)
        thm = thm.remove_reflexivity_assumptions()
        return thm

class LemmaDatabase:
    def __init__(self, main):
        self.main = main
        self.lemmata = []
        self.lemmata_s = set() # only to avoid adding duplicities

    def add(self, proven):
        lemma = Lemma(self.main, proven)
        if lemma in self.lemmata_s: return
        self.lemmata.append(lemma)
        self.lemmata_s.add(lemma)

    def find(self, goal, include_red):
        candidates = []

        # print(f"searching among {len(self.lemmata)} lemmata")
        goal = Lemma(self.main, goal, is_goal = True, include_red = include_red)
        for lemma_i,lemma in enumerate(self.lemmata):
            thm = lemma.get_thm(goal)
            if thm is not None: candidates.append((thm, lemma_i))
        if not candidates:
            return None,None
        res = min(
            candidates,
            key = lambda thm_i: (len(thm_i[0].strategy.nodes), len(thm_i[0].clause.assumptions))
        )
        # print(res[1])
        return res

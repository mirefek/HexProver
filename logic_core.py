import itertools
from weakref import WeakValueDictionary

from prop_logic import *
from strategy import *

class LogicError(Exception):
    pass

class Proof:
    def __init__(self, rule, args):
        self.rule = rule
        self.args = tuple(
            arg.proof if isinstance(arg, Theorem) else arg
            for arg in args
        )

class Theorem:
    def __init__(self, strategy, clause, proof):
        self.strategy = strategy
        self.clause = clause
        self.proof = proof
        self.nodes = self.clause.nodes | self.strategy.nodes
        assert isinstance(strategy, StrategyCombined)
        assert isinstance(clause, Clause)

    def __and__(self, other):
        return thm_resolution(self, other)

    def remove_reflexivity_assumptions(self):
        # remove reflexivity assumptions tat could appear by gluing
        refl_thms = []
        for atom in self.clause.assumptions:
            if isinstance(atom, AtomConnected) and len(atom.nodes) == 1:
                [n] = atom.nodes
                refl_thms.append(reflexivity(n))
        thm = self
        for refl_thm in refl_thms:
            thm = thm & refl_thm
        return thm

    def map_nodes(self, homo, conflict_to_red = False):
        if not isinstance(homo, dict):
            homo = { i : x for i,x in enumerate(homo) }
        thm = self
        if conflict_to_red:
            used = set()
            double = set()
            for x in self.strategy.nodes:
                y = homo.get(x,x)
                if y in used: double.add(y)
                else: used.add(y)
            if double:
                double_src = [
                    x
                    for x in self.strategy.nodes
                    if homo.get(x,x) in double
                ]
                thm = self.release_red_nodes(double_src)

        return thm_map_nodes(thm, homo)

    def release_red_nodes(self, nodes):
        return thm_release_red_nodes(self, nodes)

    def split_node(self, node, node2, node2_neighbors):
        return thm_split_node(self, node, node2, node2_neighbors)

    def __str__(self):
        nodes = sorted(self.strategy.nodes)
        if nodes:
            nodes_str = '('+', '.join(map(str, nodes))+'): '
        else:
            nodes_str = ''
        return nodes_str + str(self.clause)

# basic inference rules
def thm_resolution(thm1 : Theorem, thm2 : Theorem, atom : Atom = None):
    if atom is None:
        atoms = thm1.clause.assumptions & thm2.clause.corollaries
        if len(atoms) == 0:
            raise LogicError(f"No atom to resolve {thm1.clause} with {thm2.clause}")
        if len(atoms) > 1:
            raise LogicError(f"Ambiguous resolution of {thm1.clause} with {thm2.clause}")
        [atom] = atoms
    try:
        strategy = thm1.strategy | thm2.strategy
    except AssertionError:
        raise LogicError("Incompatible strategies")

    clause = thm1.clause.resolution(thm2.clause, atom)
    proof = Proof(thm_resolution, (thm1, thm2, atom))
    return Theorem(strategy, clause, proof)

def thm_map_nodes(thm : Theorem, homo : dict):
    assert all(isinstance(x, int) for x in homo.keys())
    assert all(isinstance(x, int) for x in homo.values())
    simp_homo = {
        a:b for a,b in homo.items()
        if a != b and a in thm.clause.nodes or a in thm.strategy.nodes
    }
    if not simp_homo: return thm
    mapped = set(homo.keys())
    if not (thm.clause.nodes <= mapped and thm.strategy.nodes <= mapped):
        homo_partial = homo
        homo = { x : x for x in thm.nodes }
        homo.update(homo_partial)
    try:
        strategy = thm.strategy.map_nodes(homo)
    except AssertionError:
        raise LogicError("Cannot contract nodes under a strategy")
    clause = thm.clause.map_nodes(homo)
    proof = Proof(thm_map_nodes, (thm, simp_homo))
    return Theorem(strategy, clause, proof)

def thm_release_red_nodes(thm : Theorem, nodes : frozenset):
    assert all(isinstance(x, int) for x in nodes)
    nodes = frozenset(nodes)
    strategy = thm.strategy.ignore_nodes(nodes)
    clause = Clause(
        frozenset(atom_is_red(n) for n in nodes) | thm.clause.assumptions,
        thm.clause.corollaries
    )
    proof = Proof(thm_release_red_nodes, (thm, nodes))
    return Theorem(strategy, clause, proof)    

# propositional axioms
def clause_intro_pos(atom_cl : Atom, atom : Atom):
    assert isinstance(atom_cl, AtomClause)
    proof = Proof(clause_intro_pos, (atom_cl, atom))
    return Theorem(empty_strategy, atom_cl.intro_pos(atom), proof)
def clause_intro_neg(atom_cl : Atom, atom : Atom):
    assert isinstance(atom_cl, AtomClause)
    proof = Proof(clause_intro_neg, (atom_cl, atom))
    return Theorem(empty_strategy, atom_cl.intro_neg(atom), proof)
def clause_elim(atom_cl : Atom):
    assert isinstance(atom_cl, AtomClause)
    proof = Proof(clause_elim, (atom_cl,))
    return Theorem(empty_strategy, atom_cl.elim(), proof)

# the following two could be derived from the previous axoims but a bit annoying
def tautology(atom : Atom):
    assert isinstance(atom, Atom)
    proof = Proof(tautology, (atom,))
    return Theorem(empty_strategy, Clause([atom], [atom]), proof)
def extend_clause(thm : Theorem, clause : Clause):
    clause = Clause(
        thm.clause.assumptions | clause.assumptions,
        thm.clause.corollaries | clause.corollaries,
    )
    simp_clause = Clause(
        clause.assumptions - thm.clause.assumptions,
        clause.corollaries - thm.clause.corollaries,
    )
    proof = Proof(extend_clause, (simp_clause,))
    return Theorem(empty_strategy, clause, proof)

# also could be simple axioms modified with map_nodes but whatever
def reflexivity(node : int):
    assert isinstance(node, int)
    proof = Proof(reflexivity, (node,))
    return Theorem(empty_strategy, atom_connected([node]).to_clause(), proof)
def transitivity(a : int, b : int, c : int):
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)
    return Theorem(
        empty_strategy,
        Clause(
            [ atom_connected(a,b), atom_is_red(b), atom_connected(b,c) ],
            [ atom_connected(a,c) ],
        ),
        Proof(transitivity, (a,b,c)),
    )

# sophisticated strategy building step
def build_case_strategy(*args):
    assert len(args) > 0
    assert len(args)%2 == 0
    red_moves = args[0::2]
    assert all(isinstance(x, int) for x in red_moves)
    thms = args[1::2]
    assert all(isinstance(move, int) for move in red_moves), red_moves
    assert all(isinstance(thm, Theorem) for thm in thms), thms

    nodes = set()
    strategy_nodes = [
        thm.strategy.nodes | set((red,))
        for red, thm in zip(red_moves, thms)
    ]
    remaining_nodes = set.union(*strategy_nodes)
    node_tuple = tuple(sorted(remaining_nodes))
    node_to_i = { node:i for i,node in enumerate(node_tuple) }
    strategies = [
        thm.strategy.map_nodes(node_to_i)
        for thm in thms
    ]
    blue_to_action = [None]*len(node_tuple)
    for red, strategy, str_nodes in zip(red_moves, strategies, strategy_nodes):
        for blue in remaining_nodes - str_nodes:
            blue_to_action[node_to_i[blue]] = node_to_i[red], strategy
            remaining_nodes.remove(blue)
    if remaining_nodes:
        raise LogicError(f"Some moves not handled: {remaining_nodes}")
    blue_to_action = tuple(blue_to_action)
    strategy = strategy_cases(node_tuple, blue_to_action)
    strategy_comb = strategy_combined([strategy])

    assumptions = frozenset(itertools.chain.from_iterable(
        thm.clause.assumptions - frozenset((atom_is_red(red),))
        for red,thm in zip(red_moves,thms)
    ))
    corollaries = frozenset(itertools.chain.from_iterable(
        thm.clause.corollaries
        for thm in thms
    ))
    clause = Clause(assumptions, corollaries)

    proof = Proof(build_case_strategy, args)
    return Theorem(strategy_comb, clause, proof)

def thm_split_node(thm : Theorem, node : int, node2 : int, node2_neighbors : frozenset):
    assert isinstance(node, int)
    assert isinstance(node2, int)
    assert all(isinstance(x, int) for x in node2_neighbors)
    node2_neighbors = frozenset(node2_neighbors)
    assumptions = set()
    def convert_assump(assump):
        if not isinstance(assump, (AtomIsRed, AtomConnected)):
            raise LogicError("No nested clauses allowed for splitting a node")
        if isinstance(assump, AtomConnected) and node in assump.nodes:
            neighbor = assump.other_node(node)
            if neighbor in node2_neighbors:
                return atom_connected(node2, neighbor)
        return assump
    assumptions = frozenset(map(convert_assump, thm.clause.assumptions))
    corollaries = set()
    for cor in thm.clause.corollaries:
        if isinstance(cor, AtomIsRed): corollaries.add(cor)
        else:
            if node not in cor.nodes:
                raise LogicError("All goals must contain the splitted node")
            neighbor = cor.other_node(node)
            corollaries.add(cor)
            corollaries.add(atom_connected(node2, neighbor))

    clause = Clause(assumptions, corollaries)
    proof = Proof(thm_split_node, (thm, node, node2, node2_neighbors))
    return Theorem(thm.strategy, clause, proof)

def thm_ignore_enpoints_red(thm : Theorem):
    if len(thm.clause.corollaries) != 1:
        raise LogicError(f"ignoring red enbpoints require exactly one corollary")
    [goal] = thm.clause.corollaries
    if not (isinstance(goal, AtomConnected)):
        raise LogicError(f"goal must be a connection")
    if not all(isinstance(x, AtomConnected, AtomRed) for x in thm.clause.assumptions):
        raise LogicError(f"assumptions must be simple")
    removed_red = frozenset(atom_is_red(n) for n in goal)
    assumptions = thm.clause.assumptions - removed_red
    clause = Clause(assumptions, thm.clause.corollaries)
    proof = Proof(thm_ignore_enpoints_red, (thm,))
    return Theorem(thm.strategy, clause, proof)

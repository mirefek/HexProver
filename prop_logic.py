
from weakref import WeakValueDictionary

class Atom:
    def to_clause(self, positive = True):
        if positive: return Clause((), (self,))
        else: return Clause((self,), ())
    @staticmethod
    def parse(s):
        if s.startswith("Red"): return AtomIsRed.parse(s)
        elif s.startswith('(') and s.endswith(')'): return AtomClause.parse(s)
        elif ' ' not in s and '-' in s: return AtomConnected.parse(s)

def get_str_inside(s, prefix, suffix):
    assert s.startswith(prefix) and s.endswith(suffix), (s,prefix, suffix)
    return s[len(prefix) : len(s)-len(suffix)]

class AtomIsRed(Atom):
    def __init__(self, node):
        self.node = node
        self.nodes = frozenset((node,))

    def map_nodes(self, homo):
        if homo[self.node] == self.node: return self
        return atom_is_red(homo[self.node])
    def __str__(self):
        return f"Red({self.node})"
    @staticmethod
    def parse(s):
        node = int(get_str_inside(s, 'Red(', ')'))
        return atom_is_red(node)

# memoized AtomIsRed
_atom_is_red_cache = WeakValueDictionary()
def atom_is_red(node):
    res = _atom_is_red_cache.get(node)
    if res is None:
        res = AtomIsRed(node)
        _atom_is_red_cache[node] = res
    return res

class AtomConnected(Atom):
    def __init__(self, nodes):
        assert isinstance(nodes, frozenset)
        self.nodes = nodes
        assert len(self.nodes) <= 2
    @classmethod
    def mk(cls, *args):
        if len(args) == 1: nodes = args[0]
        else: nodes = args
        return get_atom(cls, frozenset(nodes))

    def other_node(self, node):
        if len(self.nodes) == 1:
            [n] = self.nodes
            assert n == node
            return node
        else:
            [a,b] = self.nodes
            if a == node: return b
            else:
                assert b == node
                return a

    def map_nodes(self, homo):
        if all(homo[n] == n for n in self.nodes): return self
        return atom_connected(homo[n] for n in self.nodes)
    def __str__(self):
        if len(self.nodes) == 1:
            [a] = self.nodes
            b = a
        else:
            a,b = sorted(self.nodes)
        return f"{a}-{b}"
    @staticmethod
    def parse(s):
        a,b = s.split('-')
        return atom_connected(int(a),int(b))

# memoized AtomConnected
_atom_connected_cache = WeakValueDictionary()
def atom_connected(*args):
    if len(args) == 1: nodes = frozenset(args[0])
    else: nodes = frozenset(args)
    res = _atom_connected_cache.get(nodes)
    if res is None:
        res = AtomConnected(nodes)
        _atom_connected_cache[nodes] = res
    return res

class AtomClause(Atom):
    def __init__(self, assumptions, corollaries):
        assert isinstance(assumptions, frozenset)
        assert isinstance(corollaries, frozenset)
        self.clause = Clause(assumptions, corollaries)
        self.nodes = frozenset(self.clause.nodes)

    def intro_pos(self, atom):
        assert atom in self.clause.corollaries
        return Clause([atom], [self])
    def intro_neg(self, atom):
        assert atom in self.clause.assumptions
        return Clause((), [self, atom])
    def elim(self):
        return Clause(
            self.clause.assumptions | frozenset((self,)),
            self.clause.corollaries,
        )
    def map_nodes(self, homo):
        if all(homo[n] == n for n in self.nodes): return self
        return atom_clause(
            (a.map_nodes(homo) for a in self.clause.assumptions),
            (c.map_nodes(homo) for c in self.clause.corollaries),
        )

    def __str__(self):
        return f"({self.clause})"
    @staticmethod
    def parse(s):
        clause = Clause.parse(get_str_inside(s, '(', ')'))
        return clause_to_atom()

# memoized AtomClause
_atom_clause_cache = WeakValueDictionary()
def atom_clause(assumptions, corollaries):
    assumptions = frozenset(assumptions)
    corollaries = frozenset(corollaries)
    key = assumptions, corollaries
    res = _atom_clause_cache.get(key)
    if res is None:
        res = AtomClause(assumptions, corollaries)
        _atom_clause_cache[key] = res
    return res

class Clause:
    def __init__(self, assumptions, corollaries):
        self.assumptions = frozenset(assumptions)
        self.corollaries = frozenset(corollaries)
        self.nodes = set()
        for atom in self.assumptions:
            self.nodes |= atom.nodes
        for atom in self.corollaries:
            self.nodes |= atom.nodes
    def to_atom(self):
        return atom_clause(self.assumptions, self.corollaries)
    def resolution(self, other, atom):
        return Clause(
            (self.assumptions- frozenset((atom,))) | other.assumptions,
            (other.corollaries-frozenset((atom,))) | self.corollaries,
        )
    def map_nodes(self, homo):
        if all(homo[n] == n for n in self.nodes): return self
        return Clause(
            (a.map_nodes(homo) for a in self.assumptions),
            (c.map_nodes(homo) for c in self.corollaries),
        )        

    def __le__(self, other):
        return self.assumptions <= other.assumptions and self.corollaries <= other.corollaries

    def __str__(self):
        substrs = list(map(str, self.assumptions))
        if not self.corollaries: collorary_str = "False"
        else: collorary_str = " || ".join(map(str, self.corollaries))
        substrs.append(collorary_str)
        return " => ".join(substrs)
    @staticmethod
    def parse(s):
        assumptions_str = s.split(' => ')
        corollary_str = assumptions_str.pop()
        assumptions = frozenset(Atom.parse(x) for x in assumptions_str)
        if corollary_str == "False": corollaries = frozenset()
        else:
            corollaries = frozenset(Atom.parse(x) for x in corollary_str.split(' || '))
        return Clause(assumptions, corollaries)

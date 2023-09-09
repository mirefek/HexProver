import numpy as np
import itertools
from prop_logic import atom_connected, atom_is_red, Clause
import logic_core as core

def np_all_positions(shape):
    return np.moveaxis(np.indices(shape), 0, -1)
def positions_true(a):
    return tuple(map(tuple, np_all_positions(a.shape)[a]))

identity_transform = lambda y,x : (y,x)
def affine_transform(shift_y, shift_x, angle = 0, flip = False):
    base_yy, base_yx, base_xy, base_xx = [
        [1,0,0,1],
        [0,-1,1,1],
        [-1,-1,1,0],
        [-1,0,0,-1],
        [0,1,-1,-1],
        [1,1,-1,0],
    ][angle]
    def transform(y,x):
        y,x = base_yy*y + base_yx*x, base_xy*y + base_xx*x
        if flip: x = -x
        return y+shift_y, x+shift_x
    return transform

class HexDiagram:
    def __init__(
            self,
            available_mask, red_mask, up_mask, down_mask, # boolean np arrays of equal shapes
            up_edge, down_edge, # booleans
            extra_edges = (),
    ):
        self.shape = available_mask.shape
        self.height, self.width = self.shape
        for mask in available_mask, red_mask, up_mask, down_mask:
            assert mask.shape == self.shape
            assert mask.dtype == bool
        assert not (up_mask & down_mask).any()
        assert up_edge or up_mask.any()
        assert down_edge or down_mask.any()
        self.up_edge = up_edge
        self.down_edge = down_edge
        self.up_mask = up_mask
        self.down_mask = down_mask
        self.red_mask = red_mask & (~self.up_mask) & (~self.down_mask)
        self.empty_mask = available_mask & (~red_mask) & (~self.up_mask) & (~self.down_mask)
        self.available_mask = self.up_mask | self.down_mask | self.red_mask | self.empty_mask
        self.thm = None
        inside_nodes = self._enumerate_nodes()
        self.extra_edges = tuple(
            (a,b)
            for a,b in extra_edges
            if self.available_mask[a] and self.available_mask[b]
        )
        self._calculate_edges()
        self._contract_components(inside_nodes)
        self._make_clause()
        self.kwargs = {
            'available_mask' : self.available_mask,
            'red_mask' : self.red_mask,
            'up_mask' : self.up_mask,
            'down_mask' : self.down_mask,
            'up_edge' : self.up_edge,
            'down_edge' : self.down_edge,
            'extra_edges' : self.extra_edges,
        }

    def add_theorem(self, thm):
        if thm.clause <= self.clause:
            if not (thm.strategy.nodes <= self.empty_nodes):
                extra_nodes = thm.strategy.nodes - self.empty_nodes
                thm = thm.release_red_nodes(extra_nodes)
                if not (extra_nodes <= self.red_nodes):
                    extra_nodes -= self.red_nodes
                    thm = thm.map_nodes({ n : self.up_node for n in extra_nodes })
            self.thm = thm
        else:
            print(self.to_str('enum'))
            print("Extra literals:")
            print(Clause(thm.clause.assumptions - self.clause.assumptions, thm.clause.corollaries - self.clause.corollaries))
            raise Exception("Theorem doesn't fit the diagram")

    def _enumerate_nodes(self):
        self.up_node = 0
        inside_nodes = positions_true(self.empty_mask | self.red_mask)
        self.down_node = len(inside_nodes)+1
        self.num_nodes = len(inside_nodes)+2

        self.pos_to_node = np.zeros(self.shape, dtype = int)
        for i,pos in enumerate(inside_nodes):
            self.pos_to_node[pos] = i+1
        self.pos_to_node[self.up_mask] = self.up_node
        self.pos_to_node[self.down_mask] = self.down_node
        return inside_nodes

    def _calculate_edges(self):
        self.edges = set()

        # inner edges
        vertical_slices = (slice(1,None),slice(None)), (slice(None,-1),slice(None))
        horizontal_slices = (slice(None),slice(1,None)), (slice(None),slice(None,-1))
        diagonal_slices = (slice(1,None),slice(None,-1)), (slice(None,-1),slice(1,None))
        for sl1, sl2 in (vertical_slices, horizontal_slices, diagonal_slices):
            nodes = np.stack([self.pos_to_node[sl1], self.pos_to_node[sl2]], axis = -1)
            mask = self.available_mask[sl1] & self.available_mask[sl2]
            self.edges.update(
                frozenset((int(a),int(b)))
                for a,b in nodes[mask]
                if a != b
            )

        # border edges
        if self.up_edge:
            mask = self.available_mask[0] & ~self.up_mask[0]
            self.edges.update(
                frozenset((int(node), self.up_node))
                for node in self.pos_to_node[0][mask]
                if node != self.up_node
            )
        if self.down_edge:
            mask = self.available_mask[-1] & ~self.up_mask[-1]
            self.edges.update(
                frozenset((int(node), self.down_node))
                for node in self.pos_to_node[-1][mask]
                if node != self.down_node
            )

        # extra edges
        for a,b in self.extra_edges:
            a = self.pos_to_node[a]
            b = self.pos_to_node[b]
            self.edges.add(frozenset((a,b)))

    def _relabel_nodes(self, relabeling): # assuming relabeling is a list of new labels
        self.up_node = relabeling[self.up_node]
        self.down_node = relabeling[self.down_node]
        self.pos_to_node = np.array(relabeling)[self.pos_to_node]
        new_edges = set()
        for a,b in self.edges:
            a = relabeling[a]
            b = relabeling[b]
            if a == b: continue
            new_edges.add(frozenset((a,b)))
        self.edges = new_edges
        self.num_nodes = max(relabeling)+1

    def _contract_components(self, inside_nodes):
        red_nodes = set(int(n) for n in self.pos_to_node[self.red_mask])
        red_nodes.update((self.up_node, self.down_node))
        node_to_neighbors = [[] for _ in range(self.num_nodes)]
        for a,b in self.edges:
            if a in red_nodes and b in red_nodes:
                node_to_neighbors[a].append(b)
                node_to_neighbors[b].append(a)
        components = []
        node_to_component = [None] * self.num_nodes
        for n in range(self.num_nodes):
            if node_to_component[n] is not None: continue
            stack = [n]
            comp = len(components)
            cur_comp = []
            components.append(cur_comp)
            while stack:
                n = stack.pop()
                if node_to_component[n] is not None: continue
                node_to_component[n] = comp
                cur_comp.append(n)
                stack.extend(node_to_neighbors[n])

        # make down node last
        down = node_to_component[self.down_node]
        if down > 0 and down < len(components)-1:
            last = len(components)-1
            for n,c in enumerate(node_to_component):
                if c > down:
                    node_to_component[n] -= 1
                elif c == down:
                    node_to_component[n] = last
            components.append(components.pop(down))

        self.components = [
            [
                inside_nodes[node-1]
                for node in comp
                if node in range(1, self.num_nodes-1)
            ]
            for comp_i, comp in enumerate(components)
        ]

        if len(components) != self.num_nodes:
            self._relabel_nodes(node_to_component)

    def _make_clause(self):

        self.empty_nodes = set(int(n) for n in self.pos_to_node[self.empty_mask])
        self.red_nodes = set(int(node) for node in self.pos_to_node[self.red_mask])
        self.red_nodes.add(self.up_node)
        self.red_nodes.add(self.down_node)

        self.clause = Clause([
            atom_is_red(node)
            for node in self.red_nodes
        ] + [
            atom_connected(edge) for edge in self.edges
        ], [
            atom_connected(self.up_node, self.down_node)
        ])

    def __str__(self):
        if self.thm is None: last_line = "(draft)"
        else: last_line = "Proven!"
        return self.to_str() + '\n' + last_line
    def to_str(self, *args, **kwargs):
        return '\n'.join(self.to_lines(*args, **kwargs))
    def to_lines(self, node_names = None, up_label = '', down_label = '', skip_symbol = 'X'):
        if node_names is None:
            node_names = np.full(self.shape, None, dtype = object)
            node_names[self.up_mask] = [' A ']
            node_names[self.down_mask] = [' V ']
            node_names[self.red_mask] = [' O ']
            node_names[self.empty_mask] = [' . ']
        elif isinstance(node_names, str) and node_names == 'enum':
            node_names = np.full(self.shape, None, dtype = object)
            node_names[self.up_mask] = ['/'+str(n)+'\\' for n in self.pos_to_node[self.up_mask]]
            node_names[self.down_mask] = ['\\'+str(n)+'/' for n in self.pos_to_node[self.down_mask]]
            node_names[self.red_mask] = ['('+str(n)+')' for n in self.pos_to_node[self.red_mask]]
            node_names[self.empty_mask] = [' '+str(n)+' ' for n in self.pos_to_node[self.empty_mask]]
            up_label = str(self.up_node)
            down_label = str(self.down_node)
        else: node_names = np.array(node_names, dtype = object)

        # align sizes
        nnones_mask = (node_names != None)
        max_size = max(len(x) for x in node_names[nnones_mask])
        indent_size = max_size//2 + 1
        max_size = indent_size*2 - 1
        node_names[nnones_mask] = [' '*(max_size-len(x))+x for x in node_names[nnones_mask]]
        indent_str = ' '*indent_size

        lines = []
        indents = []
        # fill in the skip symbol, and convert to indented strings
        skip_str = (
            (1+max_size-len(skip_symbol))//2 *' ' +
            skip_symbol +
            (max_size-len(skip_symbol))//2 * ' '
        )
        for i,line in enumerate(node_names):
            line_nones = (line == None)
            [nz] = np.nonzero(~line_nones)
            if len(nz) == 0:
                lines.append('')
                indents.append(np.inf)
                continue
            begin = nz[0]
            end = nz[-1]+1
            line_nones[0:begin] = False
            line_nones[end:] = False
            line[line_nones] = [skip_str]
            indents.append(2*begin+i)
            lines.append(' '.join(line[begin:end]))

        if not lines:
            lines = ['']
            indents = [0]

        min_indent = min(indents)
        # final conversion into strings
        indents = [indent - min_indent for indent in indents]
        lines_str = []

        def add_border(indent, line, label):
            if not line:
                size = 10
                indent = 0
            else: size = len(line)
            size = max(size, len(label)+2)
            num_minuses = size - len(label)
            minuses_l = (num_minuses+1)//2 * '-'
            minuses_r = num_minuses//2 * '-'
            lines_str.append(
                indent_str*indent + minuses_l + label + minuses_r
            )

        if self.up_edge: add_border(indents[0], lines[0], up_label)
        for indent, line in zip(indents, lines):
            if not line: lines_str.append('')
            else: lines_str.append(indent_str*indent + line)
        if self.down_edge: add_border(indents[-1], lines[-1], down_label)

        return lines_str

    @staticmethod
    def parse(s):
        lines_str = s.split('\n')
        while lines_str and not lines_str[-1].strip(): del lines_str[-1]
        while lines_str and not lines_str[0].strip(): del lines_str[0]
        return HexDiagram.parse_lines(lines_str)

    @staticmethod
    def parse_file(fname):
        diagrams = []
        lines = []
        start = 1
        with open(fname) as f:
            for line_i,line in enumerate(f):
                if ';' in line: line = line[:line.index(';')]
                elif line[-1] == '\n': line = line[:-1]
                if line.strip():
                    lines.append(line)
                else:
                    if lines:
                        try:
                            diagram = HexDiagram.parse_lines(lines)
                        except:
                            print(f"Error on lines {start} -- {line_i-1}")
                            raise
                        diagrams.append(diagram)
                        lines = []
                    start = line_i+1
        if lines:
            try:
                diagram = HexDiagram.parse_lines(lines)
            except:
                print(f"Error on lines {start} -- {line_i}")
                raise
            diagrams.append(diagram)
        return diagrams

    @staticmethod
    def parse_lines(lines_str):
        symbol_to_arud = { # available, red, up, down
            'A' : [1,1,1,0],
            'V' : [1,1,0,1],
            'O' : [1,1,0,0],
            '.' : [1,0,0,0],
            'X' : [0,0,0,0],
        }

        lines_str = list(lines_str)
        def is_hline(s):
            return all(x == '-' for x in s.strip())
        if lines_str and is_hline(lines_str[0]):
            del lines_str[0]
            up_edge = True
        else:
            up_edge = False
        if lines_str and is_hline(lines_str[-1]):
            del lines_str[-1]
            down_edge = True
        else:
            down_edge = False

        # parse main lines
        if not lines_str: raise Exception("Empty diagram")
        def get_offset(input_indices1, input_indices2):
            if input_indices1[0] < input_indices2[0]:
                indices1,indices2 = input_indices1,input_indices2
            else:
                indices1,indices2 = input_indices2,input_indices1
            i = 1
            while i < len(indices1) and indices1[i] < indices2[0]:
                i += 1
            requirements = itertools.chain(
                zip(indices2, indices1[i:]),
                zip(indices1[i:], indices2[1:]),
            )
            if not all(a < b for a,b in requirements):
                raise Exception(f"Not a triangular grid: {input_indices1}, {input_indices2}")
            if indices1 is input_indices1: return i-1
            else: return -i

        offsets = []
        prev_indices = [-1]
        offset = 0
        data = []
        for line_str in lines_str:
            indices = []
            line_data = []
            for i,x in enumerate(line_str):
                if x == ' ': continue
                d = symbol_to_arud.get(x)
                if d is None: raise Exception(f"Unexpected symbol '{x}'")
                indices.append(i)
                line_data.append(d)
            if not indices: raise Exception("Diagram cannot contain an empty line")

            offset += get_offset(prev_indices, indices)
            prev_indices = indices

            offsets.append(offset)
            data.append(line_data)
        del offset

        # align to a rectangle
        min_offset = min(offsets)
        offsets = [offset - min_offset for offset in offsets]
        max_size = max(offset + len(line) for offset, line in zip(offsets, data))
        empty = [(0,0,0,0)]
        data = [
            empty * offset + line + empty * (max_size - offset - len(line))
            for offset, line in zip(offsets, data)
        ]
        data = np.array(data, dtype = bool)
        
        available_mask, red_mask, up_mask, down_mask = np.transpose(data, (2,0,1))

        return HexDiagram(available_mask, red_mask, up_mask, down_mask, up_edge, down_edge)

    def align_with(self, transform, other, debug = False): # returns dict node -> set of nodes
        if self.up_edge: start_y = -1
        else: start_y = 0
        if self.down_edge: end_y = self.height+1
        else: end_y = self.height

        res = dict()
        for src_y in range(start_y, end_y):
            for src_x in range(self.width):
                if src_y < 0: src_node = self.up_node
                elif src_y >= self.height: src_node = self.down_node
                elif self.available_mask[src_y,src_x]: src_node = int(self.pos_to_node[src_y,src_x])
                else: continue
                if src_node in res: images = res[src_node]
                else:
                    images = set()
                    res[src_node] = images

                dest_y,dest_x = transform(src_y, src_x)
                if not (0 <= dest_x < other.width):
                    continue
                elif dest_y < 0:
                    if not other.up_edge: continue
                    else: dest_node = other.up_node
                elif dest_y >= other.height:
                    if not other.down_edge: continue
                    else: dest_node = other.down_node
                elif not other.available_mask[dest_y,dest_x]:
                    continue
                else:
                    dest_node = int(other.pos_to_node[dest_y,dest_x])

                images.add(dest_node)

        if debug:
            xs = sorted(res.keys())
            for x in xs:
                print(f"{x} -> {res[x]}")
        return res

    def align_map(self, transform, other):
        alignment = self.align_with(transform, other)
        return {
            x : min(ys)
            for x,ys in alignment.items()
            if ys
        }

if __name__ == "__main__":
    
    diagrams = HexDiagram.parse_file("templates-drking.txt")
    for i,diagram in enumerate(diagrams):
        print(f"Diagram {i}")
        print(diagram)
        print()

    ziggurat = HexDiagram.parse("""
          A   . 
        .   .   . 
      .   .   .   . 
    -----------------
    """)

    print(ziggurat)
    print(ziggurat.to_str('enum'))
    clause = ziggurat.clause
    print(clause)

    large_snail = HexDiagram.parse("""
    .   A   .   O   O   O   O
      O   .   O   .   .   .   O
    O   .   O   .   O   .   O
      O   .   O   .   O   .   O
    O   .   O   .   O   .   O
      O   .   O   .   O   .   O
    O   .   .   .   O   .   O
      O   .   .   O   .   O
        O   O   O   .   O
          .   .   .   O 
        -----------------
    """)
    print(large_snail.to_str('enum'))
    print(large_snail.clause)
    print(large_snail.components)

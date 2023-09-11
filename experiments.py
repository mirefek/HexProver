from prop_logic import atom_connected
from hex_diagram import *
import logic_core as core

#  0 - 1 - 2
#  3 - 4 - 5
general_fork = core.build_case_strategy(
    1, core.transitivity(0,1,2),
    4, core.transitivity(3,4,5),
)
print("general_fork:", general_fork)

#    /0\  2
#       1  \3/
bridge = general_fork.map_nodes([0,1,3,0,2,3])
print("bridge:", bridge)

#  1-0 || 1-8
#  /1\ 3  5  7  8
#   2  4  6
# 0--------------
_open_ladders = [
    core.tautology(atom_connected(1,2))
]
def open_ladder(index):
    while index >= len(_open_ladders):
        n = len(_open_ladders)*2
        prev = _open_ladders[-1]
        prev2 = prev.map_nodes(
            { x : x for x in range(n) } | { n : n+1 }
        )
        _open_ladders.append(
            general_fork.map_nodes([1,n,0,1,n+1,n+2]) & prev & prev2
        )
    return _open_ladders[index]

print("open ladder 0:", open_ladder(0))
print("open ladder 3:", open_ladder(3))

#  /1\  3   5   7 
#     2   4   6  \0/
# 0-----------------
_closed_ladders = []
def closed_ladder(index):
    while index >= len(_closed_ladders):
        n = len(_closed_ladders)*2+2
        op = open_ladder(len(_closed_ladders))
        _closed_ladders.append(
            op.map_nodes({ n : 0 })
        )
    return _closed_ladders[index]

print("closed ladder 3:", closed_ladder(3))

ziggurat = HexDiagram.parse("""
      A   . 
    .   .   . 
  .   .   .   . 
-----------------
""")
#     /0\  1
#    2   3   4
#  5   6   7   8 
# -------9-------
ziggurat.add_theorem(
    bridge.map_nodes([0,2,4,9]) &
    bridge.map_nodes([2,5,6,9]) &
    bridge.map_nodes([0,1,3,4]) &
    bridge.map_nodes([4,7,8,9])
)
print("Ziggurat")
print(ziggurat)

def prove_ET_IV2b():
    diagram = HexDiagram.parse("""
       A   .
     O   .   .   .
       .   .   .   .
     .   .   .   .   .
    -------------------
    """)
    #      /0\    1 
    #   (0)    2     3     4 
    #       5     6     7     8 
    #    9    10    11    12    13 
    # --------------14-------------

    move_3 = (
        core.transitivity(0,3,14) &
        bridge.map_nodes([0,1,2,3]) &
        # ziggurat.thm.map_nodes([3,4,6,7,8,10,11,12,13,14])
        ziggurat.thm.map_nodes(ziggurat.align_map(affine_transform(1,1), diagram))
    )
    move_5_simple = core.transitivity(0,5,14) & bridge.map_nodes([5,9,10,14])
    move_5_b10 = (
        bridge.map_nodes([0,9,7,14]) &
        bridge.map_nodes([7,11,12,14]) &
        bridge.map_nodes([0,3,6,7]) &
        bridge.map_nodes([0,1,2,3]) &
        core.transitivity(0,5,6) &
        core.transitivity(0,5,9)
    )
    diagram.add_theorem(
        core.build_case_strategy(
            3, move_3,
            5, move_5_simple,
            5, move_5_b10,
        )
    )
    return diagram

ET_IV2b = prove_ET_IV2b()
print("Edge Template IV2b")
print(ET_IV2b)

def prove_tom():
    diagram = HexDiagram.parse("""
         .   .   .
       A   .   .   .   .
     O   X   .   O   .   .   .
       O   .   .   .   .   .   .
         X   .   .   .   .   .   .
       -----------------------------
    """)
    #        1     2     3 
    #    /0\    4     5     6     7 
    # (0)   X      8    (9)   10    11    12 
    #    (0)   13    14    15    16    17    18 
    #             19    20    21    22    23    24 
    #           -----------------25----------------
    
    move_4 = (
        core.transitivity(0,9,25) &
        core.transitivity(0,4,9) &
        bridge.map_nodes([4,5,8,9]) &
        ziggurat.thm.map_nodes(ziggurat.align_map(affine_transform(2,1), diagram))
        # ziggurat.thm.map_nodes([9,10,14,15,16,19,20,21,22,25])
    )
    connected_16 = bridge.map_nodes([16,21,22,25])
    connected_14_16 = core.transitivity(14,9,16) & bridge.map_nodes([9,10,15,16])
    connected_14a = (
        bridge.map_nodes([14,20,16,25]) &
        connected_14_16 & connected_16
    )
    connected_14b = (
        bridge.map_nodes([14,19,16,25]) &
        connected_14_16 & connected_16
    )
    connected_14c = bridge.map_nodes([14,19,20,25])
    connected_14_back = (
        core.transitivity(0,9,14) &
        (general_fork.map_nodes([14,13,0,9,4,0]) & bridge.map_nodes([4,5,8,9]))
    )
    move_13 = (
        core.transitivity(0,13,25) &
        bridge.map_nodes([13,19,14,25]) &
        connected_14a
    )
    move_14a = (
        core.transitivity(0,14,25) &
        connected_14_back & connected_14a
    )
    move_14b = (
        core.transitivity(0,14,25) &
        connected_14_back & connected_14b
    )
    move_14c = (
        core.transitivity(0,14,25) &
        connected_14_back & connected_14c
    )
    connected_6_back = core.build_case_strategy(
        2, core.transitivity(0,2,6) & bridge.map_nodes([0,1,4,2]) & bridge.map_nodes([2,3,5,6]),
        13, (
            core.transitivity(0,13,6) &
            (
                core.transitivity(0,13,25) &
                general_fork.map_nodes([13,19,25,13,8,6]) &
                core.transitivity(8,9,6)
            )
        )
    )
    move_6 = (
        core.transitivity(0,6,25) &
        connected_6_back &
        (
            ET_IV2b.thm.map_nodes(ET_IV2b.align_map(affine_transform(1,2), diagram)) &
            core.transitivity(6,9,15)
        )
    )

    diagram.add_theorem(
        core.build_case_strategy(
            4, move_4, 13, move_13, 6, move_6,
            14, move_14a, 14, move_14b, 14, move_14c,
        )
    )
    return diagram

tom = prove_tom()
print("Tom's Move")
print(tom)

import random

for _ in range(100):
    homo = [random.randint(0,50) for n in range(tom.num_nodes)]
    print(homo)
    thm = tom.thm.map_nodes(homo, conflict_to_red = True)

import numpy as np
import json

from hex_diagram import HexDiagram

class HexPuzzle:

    def __init__(self, diagram, start_red, first_pass):
        self.diagram = diagram
        self.start_red = start_red
        self.first_pass = first_pass

    def __str__(self):
        res = []
        if not self.start_red: res.append("; disconnect")
        if self.first_pass: res.append("; start with pass")
        res.append(self.diagram.to_str())
        return '\n'.join(res)

    @staticmethod
    def hexes_str_to_arr(shape, hexes_str):
        res = np.zeros(shape, dtype = bool)
        hexes_num = [ord(c)-ord('a') for c in hexes_str]
        for y,x in zip(hexes_num[0::2], hexes_num[1::2]):
            res[y,x] = True
        return res

    @staticmethod
    def parse_js_dict(jsd):
        height = jsd["rows"]
        width = jsd["cols"]
        shape = height, width
        available_mask = HexPuzzle.hexes_str_to_arr(shape, jsd["hexes"])
        red_mask = HexPuzzle.hexes_str_to_arr(shape, jsd["blackstones"])
        blue_mask = HexPuzzle.hexes_str_to_arr(shape, jsd["whitestones"])
        up_mask = HexPuzzle.hexes_str_to_arr(shape, jsd["arrowsUp"])
        down_mask = HexPuzzle.hexes_str_to_arr(shape, jsd["arrowsDown"])
        left_mask = HexPuzzle.hexes_str_to_arr(shape, jsd["arrowsLeft"])
        right_mask = HexPuzzle.hexes_str_to_arr(shape, jsd["arrowsRight"])
        up_edge = jsd["topLeft"]
        down_edge = jsd["bottomRight"]
        left_edge = jsd["bottomLeft"]
        right_edge = jsd["topRight"]
        first_player = jsd["firstPlayer"]
        first_pass = jsd.get("alreadyConnected", False)
        assert first_player in (1,2) # 1 = black (up-down), 2 = white (left-right)

        assert ((up_mask | down_mask) <= red_mask).all()
        assert ((left_mask | right_mask) <= blue_mask).all()
        assert not (red_mask & blue_mask).any()

        # autoswap
        swap_players = left_mask.any() or right_mask.any()
        if swap_players:
            first_player = 3-first_player
            height,height = height,width
            shape = height, width
            available_mask = available_mask.T
            red_mask, blue_mask = blue_mask.T, red_mask.T
            up_mask,left_mask = left_mask.T,up_mask.T
            down_mask,right_mask = right_mask.T,down_mask.T
            up_edge,left_edge = left_edge,up_edge
            down_edge,right_edge = right_edge,down_edge
        assert not (left_mask.any() or right_mask.any())

        # autocrop
        assert available_mask.any()
        start_y = 0
        while not available_mask[start_y].any(): start_y += 1
        end_y = height
        while not available_mask[end_y-1].any(): end_y -= 1
        start_x = 0
        while not available_mask[:,start_x].any(): start_x += 1
        end_x = width
        while not available_mask[:,end_x-1].any(): end_x -= 1
        if start_y > 0: up_edge = False
        if end_y < height: down_edge = False
        if start_x > 0: left_edge = False
        if end_x < width: right_edge = False
        if start_y > 0 or end_y < height or start_x > 0 or end_x < width:
            available_mask = available_mask[start_y:end_y, start_x:end_x]
            red_mask = red_mask[start_y:end_y, start_x:end_x]
            blue_mask = blue_mask[start_y:end_y, start_x:end_x]
            up_mask = up_mask[start_y:end_y, start_x:end_x]
            down_mask = down_mask[start_y:end_y, start_x:end_x]
            left_mask = left_mask[start_y:end_y, start_x:end_x]
            right_mask = right_mask[start_y:end_y, start_x:end_x]

        red_mask = available_mask & red_mask
        blue_mask = available_mask & blue_mask
        available_mask = available_mask & ~blue_mask

        diagram = HexDiagram(
            available_mask = available_mask,
            red_mask = red_mask,
            up_mask = up_mask,
            down_mask = down_mask,
            up_edge = up_edge,
            down_edge=  down_edge,
        )
        return HexPuzzle(
            diagram = diagram,
            start_red = (first_player == 1),
            first_pass = first_pass,
        )

    @staticmethod
    def parse_file(fname):
        with open(fname) as f:
            data = json.load(f)
        return [HexPuzzle.parse_js_dict(x) for x in data if not x.get("tutorial")]

if __name__ == "__main__":
    puzzles = HexPuzzle.parse_file("../puzzles/puzzle_data.js")
    puzzle_diagrams = [
        (i, puzzle.diagram)
        for i,puzzle in enumerate(puzzles)
        if puzzle.start_red and puzzle.first_pass
    ]
    index, diagram = puzzle_diagrams[57-1]
    print(index+1)
    print(diagram)
    # for puzzle in puzzles:
    #     print()
    #     print(puzzle)

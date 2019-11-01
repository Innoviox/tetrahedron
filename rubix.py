from dataclasses import dataclass
from enum import EnumMeta, Enum
from typing import List
from collections import deque
from itertools import starmap, combinations, chain, repeat

class Color(Enum):
    RED    = 1 # TOP
    GREEN  = 2 # LEFT
    BLUE   = 3 # BACK
    YELLOW = 4 # RIGHT
    
class Dir(Enum):
    LEFT  = 1 # also UP
    RIGHT = -1 # also DOWN

pieces = {
     0: [Color.RED, Color.GREEN, Color.YELLOW],
     1: [Color.RED, Color.YELLOW],
     2: [Color.RED],
     3: [Color.RED, Color.GREEN],
     4: [Color.GREEN],
     5: [Color.GREEN, Color.YELLOW],
     6: [Color.YELLOW],
     7: [Color.RED, Color.YELLOW, Color.BLUE],
     8: [Color.RED],
     9: [Color.RED, Color.BLUE],
    10: [Color.RED],
    11: [Color.RED, Color.GREEN, Color.BLUE],
    12: [Color.GREEN],
    13: [Color.GREEN, Color.BLUE],
    14: [Color.GREEN],
    15: [Color.GREEN, Color.BLUE, Color.YELLOW],
    16: [Color.YELLOW],
    17: [Color.YELLOW, Color.BLUE],
    18: [Color.YELLOW],
    19: [Color.BLUE],
    20: [Color.BLUE],
    21: [Color.BLUE]
}
for k, v in pieces.items(): pieces[k] = deque(v)

order = [[0, 3, 2, 1, 8, 7, 6, 5, 4],
         [0, 3, 2, 1, 8, 7, 6, 5, 4],
         [0, 1, 4, 6, 8, 3, 2, 5, 7],
         [0, 3, 1, 2, 8, 7, 6, 5, 4]]
move_arr = [[[0],  [[1, 3, 5],    [2, 4, 6]]],
            [[11], [[10, 12, 19], [3, 13, 9]]],
            [[15], [[16, 14, 20], [5, 13, 17]]],
            [[7],  [[8, 18, 21],  [1, 17, 9]]]]
sides = {i: [] for i in Color}
for n, colors in pieces.items():
    for i, c in enumerate(colors):
        sides[c].append([n, i])
side = "  {0}  \n {1}{2}{3} \n{4}{5}{6}{7}{8}\n"

class Tetra():
    def __init__(self):
        self.pieces = pieces.copy()

    def move(self, move: Color, level: int, direction: Dir):
        affected = move_arr[move.value - 1][level]
        if level == 0:
            self.pieces[affected[0]].rotate(direction.value)
            print("setting", affected[0], self.pieces[affected[0]])
            return
        self.move(move, 0, direction)
        
        for arr in affected:
            rot = deque(arr)
            rot.rotate(direction.value)
            new = [self.pieces[i] for i in rot]
            for i, j in zip(arr, new):
                j.reverse()
                print("setting", i, j)
                self.pieces[i] = j

    def __str__(self):
        s = ""
        for c in Color:
            print(c, sides[c])
            x = sorted(enumerate(sides[c]), key=lambda i: order[c.value - 1][i[0]])
            print(x)
            x = [self.pieces[j][k].name[0] for i, (j, k) in x]
            print(x)
            s += side.format(*x)
            # print(c, x)
            # s = sides[c][order[i]]
            # for i, (piece, color) in enumerate(sides[c]):
            #     s = ""
                # s += {0: "  ", 1: " "}.get(i, "")
                # s += self.pieces[piece][color].name[0]
                # s += {0: "  \n", 3: " \n", 8: "\n"}.get(i, "")
        return s
        
                
t = Tetra()
t.move(Color.RED, 1, Dir.LEFT)
print(t)

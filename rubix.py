from dataclasses import dataclass
from enum import EnumMeta, Enum
from typing import List
from collections import deque
from itertools import starmap, combinations, chain, repeat
from copy import deepcopy

class Color(Enum):
    RED    = 1 # TOP
    GREEN  = 2 # LEFT
    BLUE   = 3 # BACK
    YELLOW = 4 # RIGHT

    def next(self, direction):
        d = int(0.5 * direction.value + 0.5) # -1 -> 0, 1 -> 1
        return [[Color.YELLOW, Color.GREEN], [Color.RED, Color.BLUE],
                [Color.YELLOW, Color.GREEN], [Color.BLUE, Color.RED]][self.value - 1][d]
    
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
    13: [Color.BLUE, Color.GREEN],
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
         [0, 1, 8, 5, 2, 6, 3, 7, 4],
         [0, 1, 3, 2, 4, 8, 7, 6, 5]]
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
        self.pieces = deepcopy(pieces)

    def move(self, move: Color, level: int, direction: Dir):
        affected = move_arr[move.value - 1][level]
        if level == 0:
            self.pieces[affected[0]].rotate(direction.value)
            # print("setting", affected[0], self.pieces[affected[0]])
            return
        self.move(move, 0, direction)
        
        for arr in affected:
            rot = deque(arr)
            rot.rotate(direction.value)
            new = [self.pieces[i] for i in rot]
            for k, (i, j) in enumerate(zip(arr, new)):
                j.reverse()
                if direction == Dir.LEFT:
                    if move == Color.BLUE:
                        j.reverse()
                        pass
                        # if move in j:
                        #    j.reverse()
                    elif move in j and move.next(direction) in j:
                        j.reverse()
                elif direction == Dir.RIGHT:
                    if move == Color.YELLOW:
                        if (move in j and move.next(direction) in j):
                            j.reverse()
                    elif move not in j:
                        j.reverse() 
                # print("setting", i, j)
                self.pieces[i] = j

    def __str__(self):
        s = ""
        for c in Color:
            # print(c, sides[c])
            o = order[c.value - 1]
            # x = sorted(enumerate(sides[c]), key=lambda i: order[c.value - 1][i[0]])
            # x = [sides[c][o[i]] for i in range(len(sides[c]))]
            x = [sides[c][i] for i in o]
            # print(x)
            # print(self.pieces[5])
            # print([[i.name[0] for i in self.pieces[j]] for (j, k) in x])
            x = [self.pieces[j][k].name[0] for (j, k) in x]
            # print(x)
            s += side.format(*x)
            # print(c, x)
            # s = sides[c][order[i]]
            # for i, (piece, color) in enumerate(sides[c]):
            #     s = ""
                # s += {0: "  ", 1: " "}.get(i, "")
                # s += self.pieces[piece][color].name[0]
                # s += {0: "  \n", 3: " \n", 8: "\n"}.get(i, "")
        return s
        
def test():
    strs = {
        Color.RED: {Dir.LEFT: """  Y  
 YYY 
RRRRR
  R  
 RRR 
GGGGG
  B  
 BBB 
BBBBB
  G  
 GGG 
YYYYY""", Dir.RIGHT: """  G  
 GGG 
RRRRR
  Y  
 YYY 
GGGGG
  B  
 BBB 
BBBBB
  R  
 RRR 
YYYYY"""}, Color.GREEN: {Dir.LEFT: """  R  
 BRR 
BBBRR
  G  
 GGR 
GGRRR
  B  
 GBB 
GGGBB
  Y  
 YYY
YYYYY""", Dir.RIGHT: """  R  
 GRR 
GGGRR
  G  
 GGB 
GGBBB
  B  
 RBB 
RRRBB
  Y  
 YYY 
YYYYY"""}, Color.YELLOW: {Dir.LEFT: """  R  
 RRB 
RRBBB
  G  
 GGG 
GGGGG
  Y  
 YYY 
BBBBB
  Y  
 RYY 
RRRYY""", Dir.RIGHT: """  R  
 RRY 
RRYYY
  G  
 GGG 
GGGGG
  R  
 RRR 
BBBBB
  Y  
 BYY 
BBBYY"""}, Color.BLUE: {Dir.LEFT: """  R  
 RRR 
RRRRR
  G  
 YGG 
YYYGG
  B  
 BBG 
BBGGG
  Y  
 YYB 
YYBBB"""}}
    for c in Color:
        for d in Dir:
            t = Tetra()
            t.move(c, 1, d)
            if c not in strs: continue
            if d not in strs[c]: continue
            if ''.join(str(t).strip().split()) == ''.join(strs[c][d].strip().split()):
                print(f"passed test {c} {d}")
            else:
                print(f"failed test {c} {d}")

test()

t = Tetra()
t.move(Color.BLUE, 1, Dir.LEFT)
print(t)

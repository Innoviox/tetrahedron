from enum import Enum
from collections import deque

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
    TOP   = 0 # only used for expressing corner orientations

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
move_arr = [[[0],  [[1, 3, 5],    [2, 4, 6]]],  # rlt
            [[11], [[10, 12, 19], [3, 13, 9]]], # rtl
            [[15], [[16, 14, 20], [5, 13, 17]]],# rlt
            [[7],  [[8, 18, 21],  [1, 17, 9]]]] # ltr
corners = [[Dir.RIGHT, Dir.LEFT, Dir.TOP],
           [Dir.RIGHT, Dir.TOP, Dir.LEFT],
           [Dir.RIGHT, Dir.LEFT, Dir.TOP],
           [Dir.LEFT, Dir.TOP, Dir.RIGHT]]
revmap = {Color.RED: {
                        Dir.TOP: {Dir.RIGHT: True, Dir.LEFT: False},
                        Dir.LEFT: {Dir.RIGHT: False, Dir.LEFT: True},
                        Dir.RIGHT: {Dir.RIGHT: True, Dir.LEFT: True}
                     },
          Color.GREEN: {
                        Dir.TOP: {Dir.RIGHT: False, Dir.LEFT: True},
                        Dir.LEFT: {Dir.RIGHT: True, Dir.LEFT: False},
                        Dir.RIGHT: {Dir.RIGHT: True, Dir.LEFT: True}
                       },
          Color.BLUE: {
                        Dir.TOP: {Dir.RIGHT: False, Dir.LEFT: False},
                        Dir.LEFT: {Dir.RIGHT: False, Dir.LEFT: False},
                        Dir.RIGHT: {Dir.RIGHT: False, Dir.LEFT: False}
                       },
          Color.YELLOW: {
                        Dir.TOP: {Dir.RIGHT: True, Dir.LEFT: False},
                        Dir.LEFT: {Dir.RIGHT: False, Dir.LEFT: True},
                        Dir.RIGHT: {Dir.RIGHT: True, Dir.LEFT: True}
                       }
         }
sides = {i: [] for i in Color}
for n, colors in pieces.items():
    for i, c in enumerate(colors):
        sides[c].append([n, i])
side = "  {0}  \n {1}{2}{3} \n{4}{5}{6}{7}{8}\n"

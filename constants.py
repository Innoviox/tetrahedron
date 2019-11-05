from enum import Enum
from collections import deque

# class Color(Enum):
#     RED    = 1 # TOP
#     GREEN  = 2 # LEFT
#     BLUE   = 3 # BACK
#     YELLOW = 4 # RIGHT
#
#
# class Dir(Enum):
#     LEFT  = 1 # also UP
#     RIGHT = -1 # also DOWN
#     TOP   = 0 # only used for expressing corner orientations

import functools

class EnumMember:
    HASH = 0
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.l = len(self.name)
        self.hash = EnumMember.HASH
        EnumMember.HASH += 1

    def __repr__(self):
        return f"<{self.name}: {self.value}>"

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.hash

class MyEnum():
    def __init__(self, **names):
        self.__list = []
        for n, idx in names.items():
            em = EnumMember(n, idx)
            self.__list.append(em)
            setattr(self, n, em)

    def __iter__(self):
        return iter(self.__list)

Color = MyEnum(RED=1, GREEN=2, BLUE=3, YELLOW=4) # hash: 3, 10, 12, 24
Dir = MyEnum(LEFT=1, RIGHT=-1, TOP=0) # hash: 4, -5, 0

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
# for k, v in pieces.items(): pieces[k] = deque(v)

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

actions = {
    # 0: (Color.RED, 0, Dir.LEFT),
    1: (Color.RED, 1, Dir.LEFT),
    # 2: (Color.RED, 0, Dir.RIGHT),
    3: (Color.RED, 1, Dir.RIGHT),
    # 4: (Color.BLUE, 0, Dir.LEFT),
    5: (Color.BLUE, 1, Dir.LEFT),
    # 6: (Color.BLUE, 0, Dir.RIGHT),
    7: (Color.BLUE, 1, Dir.RIGHT),
    # 8: (Color.YELLOW, 0, Dir.LEFT),
    9: (Color.YELLOW, 1, Dir.LEFT),
    # 10: (Color.YELLOW, 0, Dir.RIGHT),
    11: (Color.YELLOW, 1, Dir.RIGHT),
    # 12: (Color.GREEN, 0, Dir.LEFT),
    13: (Color.GREEN, 1, Dir.LEFT),
    # 14: (Color.GREEN, 0, Dir.RIGHT),
    15: (Color.GREEN, 1, Dir.RIGHT),
}
# 5, 6
antithetic = {1: 3, 3: 1, 5: 7, 7: 5, 9: 11, 11: 9, 13: 15, 15: 13}

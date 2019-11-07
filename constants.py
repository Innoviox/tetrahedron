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

Color = [1, 2, 3, 4]
Dir = [1, -1, 0]

pieces = {
     0: [1, 2, 4],
     1: [1, 4],
     2: [1],
     3: [1, 2],
     4: [2],
     5: [2, 4],
     6: [4],
     7: [1, 4, 3],
     8: [1],
     9: [1, 3],
    10: [1],
    11: [1, 2, 3],
    12: [2],
    13: [3, 2],
    14: [2],
    15: [2, 3, 4],
    16: [4],
    17: [4, 3],
    18: [4],
    19: [3],
    20: [3],
    21: [3]
}
# for k, v in pieces.items(): pieces[k] = deque(v)

order = [[0, 3, 2, 1, 8, 7, 6, 5, 4],
         [0, 3, 2, 1, 8, 7, 6, 5, 4],
         [0, 1, 8, 5, 2, 6, 3, 7, 4],
         [0, 1, 3, 2, 4, 8, 7, 6, 5]]
move_arr = [[0,  [[1, 3, 5],    [2, 4, 6]]],  # rlt
            [11, [[10, 12, 19], [3, 13, 9]]], # rtl
            [15, [[16, 14, 20], [5, 13, 17]]],# rlt
            [7,  [[8, 18, 21],  [1, 17, 9]]]] # ltr
corners = [[-1, 1, 0],
           [-1, 0, 1],
           [-1, 1, 0],
           [1, 0, -1]]
revmap = {1: {
                        0: {-1: True, 1: False},
                        1: {-1: False, 1: True},
                        -1: {-1: True, 1: True}
                     },
          2: {
                        0: {-1: False, 1: True},
                        1: {-1: True, 1: False},
                        -1: {-1: True, 1: True}
                       },
          3: {
                        0: {-1: False, 1: False},
                        1: {-1: False, 1: False},
                        -1: {-1: False, 1: False}
                       },
          4: {
                        0: {-1: True, 1: False},
                        1: {-1: False, 1: True},
                        -1: {-1: True, 1: True}
                       }
         }
sides = {i: [] for i in Color}
for n, colors in pieces.items():
    for i, c in enumerate(colors):
        sides[c].append([n, i])
side = "  {0}  \n {1}{2}{3} \n{4}{5}{6}{7}{8}\n"

actions = {
    # 0: (1, 0, 1),
    1: (1, 1, 1),
    # 2: (1, 0, -1),
    3: (1, 1, -1),
    # 4: (3, 0, 1),
    5: (3, 1, 1),
    # 6: (3, 0, -1),
    7: (3, 1, -1),
    # 8: (4, 0, 1),
    9: (4, 1, 1),
    # 10: (4, 0, -1),
    11: (4, 1, -1),
    # 12: (2, 0, 1),
    13: (2, 1, 1),
    # 14: (2, 0, -1),
    15: (2, 1, -1),
}
# 5, 6
antithetic = {1: 3, 3: 1,
              5: 7, 7: 5,
              9: 11, 11: 9,
              13: 15, 15: 13}

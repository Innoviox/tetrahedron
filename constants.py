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

class MyEnumMeta(type):
    def __iter__(self):
        for i in dir(self):
            if i[0].isupper():
                yield getattr(self, i)

class EnumMember:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        print("hi")
        return f"<{self.name}: {self.value}>"

class MyEnum(metaclass=MyEnumMeta):
    def __init__(self, **names):
        for n, idx in names.items():
            setattr(self, n, EnumMember(n, idx))

Color = MyEnum(RED=1, GREEN=2, BLUE=3, YELLOW=4)
Dir = MyEnum(LEFT=1, RIGHT=-1, TOP=0)

print(list(Color))
print(Color.RED)
print("hi i have been imported")


# class B:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
# class _A:
#     def __init__(self):
#         self.index = 0
#
#     def __iter__(self):
#         return iter(self.klist)
#
#
# Color = _A()
# Color.RED = B('RED', 1)
# Color.GREEN = B('GREEN', 2)
# Color.BLUE = B('BLUE', 3)
# Color.YELLOW = B('YELLOW', 4)
# Color.klist = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
#
# Dir = _A()
# Dir.LEFT = B('LEFT', 1)
# Dir.RIGHT = B('RIGHT', -1)
# Dir.TOP = B('TOP', 0)
# Dir.klist = [Dir.LEFT, Dir.RIGHT, Dir.TOP]

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

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
    LEFT  = -1 # also DOWN
    RIGHT = 1 # also UP

move_arr = [[[0], [1, 2, 3, 4, 5, 6]],
            [[11], [3, 12, 13, 19, 9, 10]],
            [[15], [5, 16, 17, 20, 13, 14]],
            [[7], [1, 8, 9, 21, 17, 18]]]
pieces = {
     0: [Color.RED, Color.GREEN, Color.YELLOW]
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
    15: [Color.GREEN, Color.YELLOW, Color.BLUE],
    16: [Color.YELLOW],
    17: [Color.YELLOW, Color.BLUE],
    18: [Color.YELLOW],
    19: [Color.BLUE],
    20: [Color.BLUE],
    21: [Color.BLUE]
}
for k, v in pieces: pieces[k] = deque(v)

class Tetra():
    def __init__(self):
        self.pieces = pieces[:]

    def move(self, move: Color, level: int, direction: Dir):
        affected = move_arr[move.value][level]
        for i in affected:
            self.pieces[i].rotate(direction.value)

t = Tetra()
print(t.pieces)

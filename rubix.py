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
    LEFT  = 1 # also DOWN
    RIGHT = -1 # also UP

move_arr = [[[0], [[1, 3, 5], [2, 4, 6]]],
            [[11], [[10, 12, 19], [3, 9, 13]]],
            [[15], [[16, 20, 14], [5, 17, 13]]],
            [[7], [[8, 21, 18], [1, 9, 17]]]]
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
    15: [Color.GREEN, Color.YELLOW, Color.BLUE],
    16: [Color.YELLOW],
    17: [Color.YELLOW, Color.BLUE],
    18: [Color.YELLOW],
    19: [Color.BLUE],
    20: [Color.BLUE],
    21: [Color.BLUE]
}
for k, v in pieces.items(): pieces[k] = deque(v)

class Tetra():
    def __init__(self):
        self.pieces = pieces.copy()

    def move(self, move: Color, level: int, direction: Dir):
        affected = move_arr[move.value - 1][level]
        if level == 0:
            self.pieces[affected[0]].rotate(direction.value)
            return
        self.move(move, 0, direction)
        
        for arr in affected:
            rot = deque(arr)
            rot.rotate(direction.value)
            new = [self.pieces[i] for i in rot]
            for i, j in zip(arr, new):
                print("setting", i, j)
                self.pieces[i] = j
                
t = Tetra()
t.move(Color.RED, 1, Dir.LEFT)
print(t.pieces)

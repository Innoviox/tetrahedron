from dataclasses import dataclass
from enum import EnumMeta, Enum
from typing import List
from collections import deque
from itertools import starmap, combinations, chain, repeat

class Color(Enum):
    RED    = 1
    GREEN  = 2
    BLUE   = 3
    YELLOW = 4

class Move(Enum):
    TOP   = 1
    LEFT  = 2
    RIGHT = 3
    FRONT = 4

class Dir(Enum):
    LEFT  = -1 # also DOWN
    RIGHT = 1 # also UP

class Side(Enum):
    FRONT  = 1
    LEFT   = 2
    RIGHT  = 3
    BOTTOM = 4

class Piece:
    def __init__(self, colors, orientation=None):
        self.colors = deque(colors)
        self.orientation = orientation
        
    
CORNERS = [[1, 2, 4], [3, 1, 4], [3, 2, 1], [2, 4, 3]]

class Cube:
    def __init__(self):
        self.pieces = []
        self.pieces.extend(map(Piece, map(lambda i: list(map(Color, i)), CORNERS)))
        self.pieces.extend(map(Piece, combinations(Color, 2)))
        for i in range(3):
            for c in Color:
                for p in [Side.FRONT, Side.LEFT, Side.TOP]:
                    self.pieces.append(Piece(c, orientation=p))

    def move(self, move: Move, level: int, direction: Dir):
        sides = self.get_sides(move)
        if level == 1:
            piece = next(filter(lambda i: i.colors == sides, self.pieces))
            piece.colors.rotate(direction.value)
        else:
            self.move(move, level=1, direction)
            
        # sides.rotate(direction.value)
        # print(sides)
        
    def get_sides(self, move: Move):
        return deque(CORNERS[move.value - 1])

c = Cube()
print(c.pieces)

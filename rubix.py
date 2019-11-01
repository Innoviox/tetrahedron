from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import deque

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


@dataclass
class Side:
    color: Color
    pieces: List[List[Color]]

    @classmethod
    def of(cls, color):
        c = cls(color=color, pieces=[[color, color, color, color, color],
                                     [color, color, color], [color]])
        return c

class Cube:
    def __init__(self):
        self.sides = [Side.of(color) for color in Color]

    def move(self, move: Move, level: int, direction: Dir):
        sides = self.get_sides(move)
        sides.rotate(direction.value)
        print(sides)
        
    def get_sides(self, move: Move):
        return deque([[1, 2, 4], [3, 1, 4], [3, 2, 1], [2, 4, 3]][move.value - 1])

c = Cube()
c.move(Move.TOP, 1, Dir.LEFT)

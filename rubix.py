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
    
class Dir(Enum):
    LEFT  = -1 # also DOWN
    RIGHT = 1 # also UP

c = Cube()
print(c.pieces)

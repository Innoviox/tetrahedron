from .constants import *
from copy import deepcopy
from random import choice, randint

class Tetra():
    def __init__(self):
        self.pieces = deepcopy(pieces)

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
            for k, (i, j) in enumerate(zip(arr, new)):
                if revmap[move][corners[move.value - 1][k]][direction]:
                    j.reverse()
                self.pieces[i] = j

    def score(self):
        n = 0
        for i, j in pieces.items():
            n += sum(1 for k, l in zip(j, self.pieces[i]) if k == l)
        return n / 36 # 36 is max

    def random(self, n):
        for i in range(n):
            self.move(choice(list(Color)), randint(0, 1), choice([Dir.LEFT, Dir.RIGHT]))

    def __str__(self):
        # return ''.join(side.format(*[self.pieces[j][k].name[0] for (j, k) in [sides[c][i] for i in order[c.value - 1]]]) for c in Color)
        s = ""
        for c in Color:
            o = order[c.value - 1]
            x = [sides[c][i] for i in o]
            x = [self.pieces[j][k].name[0] for (j, k) in x]
            s += side.format(*x)
        return s


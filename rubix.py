from constants import *
from copy import deepcopy
from random import choice, randint
import numpy as np
from tqdm import tqdm, trange
import time
import heapq


# color_conv = {'R': Color.RED, 'G': Color.GREEN, 'Y': Color.YELLOW, 'B': Color.BLUE}

def rot(arr, direction):
    if direction == -1:
        return arr[1:] + [arr[0]]
    return [arr[-1]] + arr[:-1]
    # if direction.value == -1:
    #     return [arr[1], arr[2], arr[0]]
    # return [arr[2], arr[0], arr[1]]

class Tetra:
    def __init__(self, start=True):
        if start: self.pieces = deepcopy(pieces)

    def move(self, move: Color, level: int, direction: Dir, out=False):
        if out: print("moving", move, level, direction)

        aff0, affected = move_arr[move - 1]

        r = revmap[move]

        self.pieces[aff0] = rot(self.pieces[aff0], direction)
        if level == 0: return

        for arr in affected:
            for k, i, j in zip(corners[move - 1], arr, rot([self.pieces[i] for i in arr], direction)):
                # .reverse()
                self.pieces[i] = j[::-1] if r[k][direction] else j
        return self

    def score(self):
        n = 0
        for i, j in pieces.items():
            n += sum(1 for k, l in zip(j, self.pieces[i]) if k == l)
        return n / 36  # 36 is max

    def random(self, n=1, out=False):
        for i in range(n):
            n = randint(0, 1) if len(list(actions.keys())) == 16 else 1
            self.move(choice(list(Color)), n, choice([Dir.LEFT, Dir.RIGHT]), out=out)

    def cronkin(self):
        self.move(Color.GREEN, 1, Dir.RIGHT)
        self.move(Color.YELLOW, 1, Dir.RIGHT)
        self.move(Color.GREEN, 1, Dir.LEFT)
        self.move(Color.YELLOW, 1, Dir.LEFT)
        self.move(Color.GREEN, 1, Dir.LEFT)
        self.move(Color.RED, 1, Dir.LEFT)
        self.move(Color.GREEN, 1, Dir.RIGHT)
        self.move(Color.RED, 1, Dir.RIGHT)

    def to_space(self):
        box = np.zeros((4, 9))
        for c in Color:
            o = order[c - 1]
            x = [sides[c][i] for i in o]
            x = np.array([self.pieces[j][k] - 1 for (j, k) in x])
            box[c - 1] = x
        # print(box)
        return box

    def __str__(self):
        # return ''.join(side.format(*[self.pieces[j][k].name[0] for (j, k) in [sides[c][i] for i in order[c.value - 1]]]) for c in Color)
        s = ""
        for c in Color:
            o = order[c - 1]
            x = [sides[c][i] for i in o]
            x = [' RGBY'[self.pieces[j][k]] for (j, k) in x]
            s += side.format(*x)
        return s

    # def to_readable_string(self):
    #     return ','.join(''.join(k.name[0] for k in j) for j in self.pieces.values())

    @classmethod
    def of(cls, other):
        t = cls(start=False)
        t.pieces = other.pieces.copy()
        return t

    def copy(self):
        return Tetra.of(self)

    def is_solved(self):
        return self.pieces == pieces

    def step(self, act):
        return Tetra.of(self).move(*act)

    def solve_bfs(self):
        nodes = deque([()])
        cache = MoveCache(self)

        while nodes:
            path = nodes.popleft()
            if cache.move(path).is_solved(): return path
            nodes.extend([path + (i,) for i in actions
                          if not path or (i - path[-1] and i - antithetic[path[-1]])])

class MoveCache():
    def __init__(self, t):
        self.tetra = t
        self.cache = {None: t}

    def move(self, action):
        curr_cache = self.cache
        for i in action:
            if i not in curr_cache:
                curr_cache[i] = {None: curr_cache[None].step(actions[i])}
            curr_cache = curr_cache[i]
        return curr_cache[None]


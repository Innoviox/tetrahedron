from constants import *
from copy import deepcopy
from random import choice, randint
from gym import spaces
import numpy as np
from tqdm import tqdm
import time

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

color_conv = {'R': Color.RED, 'G': Color.GREEN, 'Y': Color.YELLOW, 'B': Color.BLUE}


class Tetra():
    def __init__(self, start=True):
        if start: self.pieces = deepcopy(pieces)

    def rot(self, arr, direction):
        if direction.value == 1:
            return arr[1:] + [arr[0]]
        return [arr[-1]] + arr[:-1]

    def move(self, move: Color, level: int, direction: Dir, out=False):
        if out: print("moving", move, level, direction)
        affected = move_arr[move.value - 1][level]
        if level == 0:
            s = self.pieces[affected[0]]
            self.pieces[affected[0]] = self.rot(s, direction)
            return
        self.move(move, 0, direction)

        for arr in affected:
            rot = self.rot(arr, direction)
            new = [self.pieces[i] for i in rot]
            for k, (i, j) in enumerate(zip(arr, new)):
                if revmap[move][corners[move.value - 1][k]][direction]:
                    j = j[::-1]
                self.pieces[i] = j
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
            o = order[c.value - 1]
            x = [sides[c][i] for i in o]
            x = np.array([self.pieces[j][k].value - 1 for (j, k) in x])
            box[c.value - 1] = x
        # print(box)
        return box

    def __str__(self):
        # return ''.join(side.format(*[self.pieces[j][k].name[0] for (j, k) in [sides[c][i] for i in order[c.value - 1]]]) for c in Color)
        s = ""
        for c in Color:
            o = order[c.value - 1]
            x = [sides[c][i] for i in o]
            x = [self.pieces[j][k].name[0] for (j, k) in x]
            s += side.format(*x)
        return s

    # def to_readable_string(self):
    #     return ','.join(''.join(k.name[0] for k in j) for j in self.pieces.values())

    @classmethod
    def of(cls, other):
        t = cls(start=False)
        t.pieces = {a: i[:] for a, i in other.pieces.items()}
        return t

    def copy(self):
        return Tetra.of(self)

    def is_solved(self):
        return self.pieces == pieces
        # return self.score() == 1

    def step(self, act):
        return Tetra.of(self).move(*act)

    def solve_dfs(self):
        def advance(curr_tetra, curr_algo):
            if len(curr_algo) > 12 or curr_tetra.is_solved():
                return curr_algo

            advances = [advance(curr_tetra.step(j), curr_algo + [i]) for i, j in actions.items()]
            return min(advances, key=len)

        return advance(self, [])


    # def solve_bfs(self):
    #     def advance(curr_tetra, curr_algo):
    #         print(curr_algo)
    #         input()
    #         if len(curr_algo) > 12:
    #             return curr_algo
    #
    #         for i, j in actions.items():
    #             print("a")
    #             next = curr_tetra.step(j)
    #             if next.is_solved():
    #                 return curr_algo + [i]
    #
    #         for i, j in actions.items():
    #             print("b")
    #             next = curr_tetra.step(j)
    #             adv = advance(next, curr_algo + [i])
    #             if len(adv) <= 12:
    #                 return adv
    #
    #         print("nothign found? wyh")
    #
    #     return advance(self, [])

    def solve_bfs(self):
        nodes = deque([()])
        cache = MoveCache(self)

        last_len = 0
        t = time.time()

        while nodes:
            path = nodes.popleft()

            if len(path) != last_len:
                print(last_len, time.time() - t)
                last_len += 1

            v = cache.move(path)
            if v.is_solved():
                return path

            nodes.extend([path + (i,) for i in actions])

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


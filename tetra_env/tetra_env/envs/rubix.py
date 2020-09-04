from constants import *
from copy import deepcopy
from random import choice, randint
from gym import spaces
import numpy as np
from tqdm import tqdm

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


class Tetra():
    def __init__(self):
        self.pieces = deepcopy(pieces)

    def move(self, move: Color, level: int, direction: Dir, out=False):
        if out: print("moving", move, level, direction)
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

    @classmethod
    def of(cls, other):
        t = cls()
        t.pieces = deepcopy(other.pieces)
        return t

    def copy(self):
        return Tetra.of(self)

    def is_solved(self):
        return self.score() == 1

    def step(self, act):
        t = self.copy()
        t.move(*act)
        return t

    def solve_dfs(self):
        def advance(curr_tetra, curr_algo):
            print(curr_algo)
            input(curr_tetra.is_solved())
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
        nodes = [[]]
        visited = []
        t = tqdm(total=1000000)
        while nodes:
            path = nodes.pop(0)

            v = Tetra.of(self)
            for p in path: v.move(*actions[p])

            if v.is_solved():
                return path

            for i in actions:
                p = path + [i]
                # if p not in visited:
                nodes.append(p)
                    # visited.append(p)
            t.update(1)
        t.close()

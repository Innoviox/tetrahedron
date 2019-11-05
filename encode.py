import pickle
from rubix import Tetra
from tqdm import trange

with open("data", "wb") as f:
    spaces, solves = [], []
    for i in trange(100):
        t = Tetra()
        t.random(n=10)

        spaces.append(t.to_space())
        solves.append(t.solve_bfs())

    pickle.dump([spaces, solves], f)


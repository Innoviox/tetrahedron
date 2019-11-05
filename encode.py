import pickle
from rubix import Tetra
from tqdm import trange

with open("data", "wb") as f:
    spaces, solves = [], []
    for i in trange(10000):
        try:
            t = Tetra()
            t.random(n=3)

            spaces.append(t.to_space())
            solves.append(t.solve_bfs())
        except KeyboardInterrupt:
            break
    print("writing")
    pickle.dump([spaces, solves], f)


import pickle
import numpy as np

spaces, _solves = pickle.load(open("data", "rb"))
spaces, _solves = np.array(spaces), np.array(_solves)

spaces = [i.flatten() for i in spaces]

solves = []
for i in _solves:
    solves.append(np.zeros(12))
    for a, b in enumerate(i):
        solves[-1][a] = b

with open("datac", "wb") as f:
    pickle.dump((spaces, solves), f)

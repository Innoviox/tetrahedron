
import profile, pstats
from rubix import Tetra, actions

t = Tetra()

# for i in [1, 7, 9, 15, 9]:
#     t.move(*actions[i])

t.random(n=20)

print(t.solve_bfs())

# cmd: pycallgraph graphviz -- ./profiles.py 


viz = False
if viz: import viz
from rubix import Tetra, actions, time

# import timeit

# def a():
#     c = Tetra()
#
# t = Tetra()
# def b():
#     c = Tetra.of(t)
# print(timeit.timeit(a, number=1000), timeit.timeit(b, number=1000))

import tests

t = Tetra()
if viz: viz.render(t)

"""
moving <GREEN: 2> 1 <LEFT: 1>
moving <RED: 1> 1 <RIGHT: -1>
moving <GREEN: 2> 1 <RIGHT: -1>
moving <GREEN: 2> 1 <RIGHT: -1>
moving <GREEN: 2> 1 <LEFT: 1>
moving <BLUE: 3> 1 <LEFT: 1>
moving <GREEN: 2> 1 <LEFT: 1>
moving <RED: 1> 1 <RIGHT: -1>
moving <BLUE: 3> 1 <LEFT: 1>
moving <GREEN: 2> 1 <LEFT: 1>

19.428097009658813
(15, 7, 3, 15, 3, 7, 1)
"""

for i in [13, 3, 15, 15, 13, 5, 13, 3, 5, 13]:
    t.move(*actions[i])

ti = time.time()
x = t.solve_bfs()
print(time.time() - ti)
print(x)
if viz:
    n = 0
    while 1:
        flag = True
        while flag:
            try:
                viz.engine.tick()
            except KeyboardInterrupt:
                if input() != 'n':
                    flag = False
                else:
                    exit()
        t.move(*actions[x[n]])
        n += 1

def viz_test():
    t = viz.Tetra()




    viz.render(t)

    # t.move(viz.Color.GREEN, 1, viz.Dir.RIGHT, out=True)



    while 1:
        flag = True
        t.random(n=50, out=True)
        while flag:
            try:
                viz.engine.tick()
            except KeyboardInterrupt:
                if input() != 'n':
                    flag = False
                else:
                    exit()

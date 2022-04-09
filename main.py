viz = True
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
print(str(t))

"""
9.689351797103882
(15, 7, 3, 15, 3, 7, 1)
"""

# for i in [13, 3, 15, 15, 13, 5, 13, 3, 5, 13]:
#     t.move(*actions[i])
#
# t.random(n=10, out=True)

# for _ in range(10):
#     t.random(n=1, out=True)
"""
    flag = True
    while flag:
        try:
            viz.engine.tick()
        except KeyboardInterrupt:
            break
    # t.move(*actions[x[n]])
"""
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

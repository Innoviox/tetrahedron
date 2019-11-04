# import viz
from rubix import Tetra, actions

import tests

t = Tetra()

# t.move(*actions[2])
# t.move(*actions[0])

t.random(n=1, out=True)

# viz.render(t)

x = t.solve_bfs()
#
print(x)
#
# n = 0
# while 1:
#     flag = True
#     while flag:
#         try:
#             viz.engine.tick()
#         except KeyboardInterrupt:
#             if input() != 'n':
#                 flag = False
#             else:
#                 exit()
#     t.move(*actions[x[n]])
#     n += 1

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

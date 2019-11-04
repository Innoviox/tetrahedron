from tetra_env import viz
from tetra_env import Tetra, actions

t = Tetra()

# t.move(*actions[2])
# t.move(*actions[0])

t.random(n=20, out=True)

print(t.solve_bfs())

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

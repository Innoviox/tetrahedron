from tetra_env import viz


t = viz.Tetra()

viz.render(t)

t.move(viz.Color.GREEN, 1, viz.Dir.RIGHT, out=True)

# t.random(n=10, out=True)

while 1:
    viz.engine.tick()

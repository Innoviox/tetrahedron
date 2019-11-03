from tetra_env import viz


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

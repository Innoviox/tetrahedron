import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .viz import render, Tetra, Color, Dir, engine

actions = {
    0: (Color.RED, 0, Dir.LEFT),
    1: (Color.RED, 1, Dir.LEFT),
    2: (Color.RED, 0, Dir.RIGHT),
    3: (Color.RED, 1, Dir.RIGHT),
    4: (Color.BLUE, 0, Dir.LEFT),
    5: (Color.BLUE, 1, Dir.LEFT),
    6: (Color.BLUE, 0, Dir.RIGHT),
    7: (Color.BLUE, 1, Dir.RIGHT),
    8: (Color.YELLOW, 0, Dir.LEFT),
    9: (Color.YELLOW, 1, Dir.LEFT),
    10: (Color.YELLOW, 0, Dir.RIGHT),
    11: (Color.YELLOW, 1, Dir.RIGHT),
    12: (Color.GREEN, 0, Dir.LEFT),
    13: (Color.GREEN, 1, Dir.LEFT),
    14: (Color.GREEN, 0, Dir.RIGHT),
    15: (Color.GREEN, 1, Dir.RIGHT),
}

# actions = {
#     0: (Color.RED, 1, Dir.LEFT),
#     1: (Color.RED, 1, Dir.RIGHT),
#     2: (Color.BLUE, 1, Dir.LEFT),
#     3: (Color.BLUE, 1, Dir.RIGHT),
#     4: (Color.YELLOW, 1, Dir.LEFT),
#     5: (Color.YELLOW, 1, Dir.RIGHT),
#     6: (Color.GREEN, 1, Dir.LEFT),
#     7: (Color.GREEN, 1, Dir.RIGHT),
#     }

class TetraEnv(gym.Env):
    metadata = {'render.modes': ['human', 'none']}

    def __init__(self):
        self.reset()
        self.action_space = spaces.Discrete(len(list(actions.keys())))
        self.observation_space = spaces.Box(low=0, high=3, shape=(4, 9))
        self.viz_set_up = False
        self.memory = []
        self.memory_length = 3
        self.last_reward = 0
        self.threshold = 0.8

    def step(self, action):  # action is number from 1-16
        self.tetra.move(*actions[action])
        
        s = self.tetra.score()

        self.last_reward = round(s, 3)
        done = s >= self.threshold
        s = int(done)
        return self.tetra.to_space(), s, done, {}

    def reset(self):
        self.tetra = Tetra()
        self.tetra.random(n=10)
        return self.tetra.to_space()

    def render(self, mode='human', close=False):
        assert mode in TetraEnv.metadata['render.modes']
        print(self.last_reward)
        if mode == 'human':
            render(self.tetra)
            engine.tick()
                

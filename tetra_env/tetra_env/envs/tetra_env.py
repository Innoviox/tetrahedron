import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .rubix import *
from .viz import render

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human', 'none']}

    def __init__(self):
        self.reset()
        self.action_space = spaces.Discrete(16)
        self.viz_set_up = False

    def step(self, action):  # action is number from 1-16
        n = bin(action)[2:]
        *act, level, direc = n
        act = Color._value2member_map_[int(''.join(act), 2)]
        level = int(level)
        direc = Dir.LEFT if direc == '0' else Dir.RIGHT
        self.tetra.move(act, level, direc)

        s = self.tetra.score()
        return self.tetra, s, s==1, {} 

    def reset(self):
        self.tetra = Tetra()
        self.tetra.random(50)
        return self.tetra

    def render(self, mode='human', close=False):
        assert mode in metadata['render.modes']
        if mode == 'none':
            return
        else:
            render(self.tetra)
                

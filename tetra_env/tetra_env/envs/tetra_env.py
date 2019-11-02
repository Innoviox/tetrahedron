import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .viz import render, Tetra, Color, Dir

class TetraEnv(gym.Env):
    metadata = {'render.modes': ['human', 'none']}

    def __init__(self):
        print("HI")
        self.reset()
        self.action_space = spaces.Discrete(16)
        self.observation_space = spaces.Box(low=0, high=3, shape=(4, 9))
        self.viz_set_up = False

    def step(self, action):  # action is number from 1-16
        # print("stepping", action)
        n = bin(action)[2:]
        try:
            *act, level, direc = n
        except ValueError:
            act = ''
            level = ''
            direc = ''
        
        if act:
            act = Color._value2member_map_[int(''.join(act), 2)]
        else:
            act = Color.RED

        if level:
            level = int(level)
        else:
            level = 0

        if direc:
            direc = Dir.LEFT if direc == '0' else Dir.RIGHT
        else:
            direc = Dir.LEFT
        
        self.tetra.move(act, level, direc)

        s = self.tetra.score()
        return self.tetra.to_space(), s, s==1, {} 

    def reset(self):
        self.tetra = Tetra()
        self.tetra.random(50)
        return self.tetra.to_space()

    def render(self, mode='human', close=False):
        assert mode in TetraEnv.metadata['render.modes']
        if mode == 'none':
            print(round(self.tetra.score(), 2))
        else:
            render(self.tetra)
                

from gym.envs.registration import register

register(
    id='tetra-v0',
    entry_point='tetra_env.envs:TetraEnv',
)

from .envs import viz
from .envs.constants import *
from .envs.rubix import *
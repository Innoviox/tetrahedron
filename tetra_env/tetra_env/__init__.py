from gym.envs.registration import register

register(
    id='tetra-v0',
    entry_point='tetra_env.envs:TetraEnv',
)
import numpy as np
import gym

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import *
from rl.memory import SequentialMemory, EpisodeParameterMemory

import tetra_env
from tetra_env import viz

ENV_NAME = 'tetra-v0'


# Get the environment and extract the number of actions.
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n
print(env.action_space, nb_actions)
print(env.observation_space)

mem_length = 1
# Next, we build a very simple model.
model = Sequential()
model.add(Flatten(input_shape=(mem_length,) + env.observation_space.shape))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
model.summary()

# Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
# even the metrics!
# memory = EpisodeParameterMemory(limit=1000, window_length=mem_length) # SequentialMemory(limit=50000, window_length=mem_length)
memory = SequentialMemory(limit=50000, window_length=mem_length)
policy = MaxBoltzmannQPolicy()
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=2000,
               train_interval=50, target_model_update=1e-2, policy=policy, enable_dueling_network=True)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

# Okay, now it's time to learn something! We visualize the training here for show, but this
# slows down training quite a lot. You can always safely abort the training prematurely using
# Ctrl + C.
dqn.fit(env, nb_steps=500000, visualize=False, verbose=1)

# After training is done, we save the final weights.
dqn.save_weights('dqn_{}_weights.h5f'.format(ENV_NAME), overwrite=True)
# dqn.load_weights('dqn_{}_weights.h5f'.format(ENV_NAME))

# Finally, evaluate our algorithm for 5 episodes.
dqn.test(env, nb_episodes=5, visualize=True, nb_max_episode_steps=20)

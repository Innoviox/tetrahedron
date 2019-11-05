import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

import numpy as np

import pickle

spaces, solves = pickle.load(open("datac", "rb"))
n = 50000
train_x, test_x = spaces[:n], spaces[n:]
train_y, test_y = solves[:n], solves[n:]

print(train_x[5], train_y[5])

model = Sequential()
# model.add(Flatten(input_shape=(4, 9)))
model.add(Dense(16, input_shape=(36,)))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(12))
model.add(Activation('softmax'))
model.summary()

model.compile(Adam(lr=1e-3), loss='mse', metrics=['accuracy'])

# model.fit(train_x, train_y, epochs=50)
# model.save('my_model.h5')

model.load_weights('my_model.h5')

# print(model.evaluate(test_x, test_y))

from rubix import Tetra

for i in range(5):
    t = Tetra()
    t.random(n=3, out=True)
    s = t.to_space().flatten()
    print(s, s.shape)
    m = model.predict(np.array([s]))[0]

    print([round(i * 20) - 1 for i in m])
    print(t.solve_bfs())

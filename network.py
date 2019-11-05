import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

import pickle

spaces, solves = pickle.load(open("data", "rb"))
train_x, test_x = spaces[:40000], spaces[40000:]
train_y, test_y = solves[:40000], solves[40000:]

model = Sequential()
model.add(Flatten(input_shape=(4, 9)))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(12))
model.add(Activation('softmax'))
model.summary()

model.compile(Adam(lr=1e-3), loss='mse', metrics=['accuracy'])

model.fit(train_x, train_y)

print(model.evaluate(test_x, test_y))

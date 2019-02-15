from keras import Sequential, losses
from keras.layers import Conv3D, Flatten, Dense

model = Sequential()
model.add(Conv3D(filters=16, kernel_size=(8, 8, 2), strides=4, activation='relu', input_shape=(350, 150, 4, 3)))
model.add(Conv3D(filters=32, kernel_size=(8, 8, 1), strides=2, activation='relu'))
model.add(Flatten())
model.add(Dense(3, activation='relu'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

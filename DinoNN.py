from keras import Sequential
from keras.layers import Conv3D, Flatten, Dense


class DinoNN(Sequential):
    def __init__(self):
        super().__init__()
        self.add(Conv3D(filters=16, kernel_size=(8, 8, 2), strides=4, activation='relu', input_shape=(350, 150, 4, 3)))
        self.add(Conv3D(filters=32, kernel_size=(8, 8, 1), strides=2, activation='relu'))
        self.add(Flatten())
        self.add(Dense(3, activation='relu'))

        self.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

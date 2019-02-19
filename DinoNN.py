import numpy as np
from keras import Sequential
from keras.layers import Conv3D, Flatten, Dense

from ImgProcessing import prepare_batch


class DinoNN(Sequential):
    def __init__(self, img_rect, n_frames=4):
        super().__init__()

        self.img_rect = img_rect
        x0, y0, x1, y1 = img_rect

        self.add(Conv3D(filters=16, kernel_size=(8, 8, 2), strides=4, activation='relu', batch_size=1,
                        input_shape=(y1 - y0, x1 - x0, n_frames, 1)))  # numpy has h x w instead of w x h
        self.add(Conv3D(filters=32, kernel_size=(8, 8, 1), strides=2, activation='relu'))
        self.add(Flatten())
        self.add(Dense(3, activation='relu'))

        self.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def map(self, batch, verbose=0):
        processed = prepare_batch(batch, self.img_rect)
        np_images = map(lambda i: np.array(i, dtype=np.float32), processed)
        x = np.stack(list(np_images), axis=2)
        reshaped = x.reshape(self.input_shape)  # add the extra dimension of channel
        return super().predict(reshaped, verbose=verbose, batch_size=1)

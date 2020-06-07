import tensorflow as tf
import os
class Model():
    def __init__(self, filepath='model.h5'):
        self.filepath = filepath
        if os.path.exists(filepath):
            self.model = tf.keras.models.load_model(filepath)
        else:

            mnist = tf.keras.datasets.mnist
            (x_train, y_train),(x_test, y_test) = mnist.load_data()
            x_train, x_test = x_train / 255.0, x_test / 255.0
            self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax')
            ])
            self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

            self.model.fit(x_train, y_train, epochs=5)
            self.model.evaluate(x_test, y_test)
    def save(self):
        self.model.save(self.filepath)
    def is_saved(self):
        return os.path.exists(self.filepath)

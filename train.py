import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt
class Model():
    def __init__(self, filepath='model.h5'):
        self.filepath = filepath
        mnist = tf.keras.datasets.mnist
        (x_train, y_train),(x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0
        self.x_test = x_test
        self.y_test = y_test

        if os.path.exists(filepath):
            self.model = tf.keras.models.load_model(filepath)
        else:
            self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
            ])
            self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

            self.model.fit(x_train, y_train, epochs=10)
            self.model.evaluate(x_test, y_test)
            self.save()
    def save(self):
        self.model.save(self.filepath)
    def predict(self, pixels):
        prediction = self.model.predict([pixels])
        return np.argmax(prediction[0])
    def examples(self, n=5):
        predictions = self.model.predict(self.x_test)
        for i in range(n):
            plt.imshow(self.x_test[i], cmap='binary')
            print("Prediction", np.argmax(predictions[i]), ", actual:", self.y_test[i])
            plt.show()
    def evaluate(self):
        self.model.evaluate(self.x_test, self.y_test)
if __name__ == '__main__':
    if os.path.exists('model.h5'):
        os.remove('model.h5')
    Model()

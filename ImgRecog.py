import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
imgs=keras.datasets.img
(x_train, y_train), (x_test, y_test) = img.load_data()
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_train, axis = 1)
tf.keras.model.Sequential()
model.add.tf.layers.Flatten(input_shape = (28,28))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))
model.compile(optimizer="adam", loss="sparse_catagorical_crossentropy", metrics = ["accuracy"])
model.fit(x_train, y_train, epochs=3)
model.save("digits_recognition.keras")

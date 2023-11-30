
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

(X_train,y_train),(X_test,y_test) = tf.keras.datasets.mnist.load_data()

cnn=tf.keras.Sequential()

cnn.add(tf.keras.layers.Conv2D(filters=64,padding='same', strides=2, kernel_size=3,activation='relu',input_shape=(28,28)))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=32, strides=2, padding='same',kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(10,activation='softmax'))
cnn.compile(optimizer=tf.keras.optimizers.legacy.Adam(),loss='categorical_crossentropy',metrics=['accuracy'])
history = cnn.fit(X_train, y_train,epochs=25,validation_split=0.2)

cnn.save("digit_recognition.h5")


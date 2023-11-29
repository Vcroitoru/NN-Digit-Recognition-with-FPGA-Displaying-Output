import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
base_dir=r"train"
IMAGE_SIZE=224
BATCH_SIZE=64

#pre=processing
train_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.1
    )

test_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
     rescale=1./255,
     validation_split=0.1
)

train_datagen=train_datagen.flow_from_directory(
    base_dir,
    target_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    subset='training'
)

test_datagen=test_datagen.flow_from_directory(
    base_dir,
    target_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    subset='validation'
)

cnn=tf.keras.Sequential()
cnn.add(tf.keras.layers.Conv2D(filters=64,padding='same',strides=2,kernel_size=3,activation='relu',input_shape=(224,224,3)))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=32,padding='same',strides=2,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=32,padding='same',strides=2,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2))


cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(10,activation='softmax'))
cnn.compile(optimizer=tf.keras.optimizers.legacy.Adam(),loss='categorical_crossentropy',metrics=['accuracy'])
history = cnn.fit(train_datagen,epochs=25,validation_data=test_datagen)

# cnn.save("digit_recognition.h5")

# plt.plot(history.history['accuracy'], label='accuracy')
# plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.ylim([0.5, 1])
# plt.legend(loc='lower right')

# test_loss, test_acc = cnn.evaluate(train_datagen, verbose=2)

# plt.savefig("output_report.png")

# import cv2
# img = cv2.imread('numba3.jpg')
# resize = tf.image.resize(img, (224,224))

# y_probs = cnn.predict(np.expand_dims(resize/255, 0))
# y_pred  = np.argmax(y_probs, axis=-1)

# print (y_probs)
# print(y_pred)


# for i in len(y_probs):
#     if (y_probs >= 0.50):

# if (y_pred[0] == 2):
#     print("Prediction: 2")
# elif (y_pred[0] == 0):
#     print("Prediction: 0")
# elif (y_pred[0] == 1):
#     print("Prediction: 1")
# elif (y_pred[0] == 3):
#     print("Prediction: 3")


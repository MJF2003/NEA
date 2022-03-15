import keras
from matplotlib import pyplot as plt

from func import *
import numpy as np
import os
import PIL
import PIL.Image
import pathlib
import tensorflow as tf
from tensorflow import keras

from keras import layers
from keras.preprocessing.image import array_to_img


data_dir = pathlib.Path("../data")  # Location of the dataset

batch_size = 3
img_height = 100
img_width = 100


train_ds = tf.keras.utils.image_dataset_from_directory(  # Define the training set from the directory
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)
val_ds = tf.keras.utils.image_dataset_from_directory(  # Same but for validation
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

class_names = train_ds.class_names  # Returns a list of the classnames defined by subdirectory titles


resize_rescale = keras.Sequential([  # Resizing the dataset components to square and correct size - not necessary in
    # this case
    layers.Resizing(img_height, img_width),
    layers.Rescaling(1./255)  # Pixel vals to between 0 and 1
])

data_augmentation = keras.Sequential([  # Augmentation creates additional examples from the defined dataset by rotating
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.2),
])

# Start of Optimisation Features
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
# End of Optimisation Fetaures

num_classes = len(class_names)  # Number of possible classes the images could fall into

model = keras.Sequential([
    resize_rescale,
    data_augmentation,
    layers.Conv2D(16, 3, padding='same', activation='sigmoid'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='sigmoid'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='sigmoid'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

epochs = 30
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

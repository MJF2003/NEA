
from matplotlib import pyplot as plt

from func import *
import pathlib
import tensorflow as tf


def build_model():
    data_dir = pathlib.Path("data")  # Location of the dataset

    batch_size = 4
    img_height = 48
    img_width = 48

    # Extract Datasets from directory
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
    num_classes = len(class_names)  # Number of possible classes the images could fall into

    resize_rescale = tf.keras.Sequential([  # Resizing the dataset components to square and correct size
        tf.keras.layers.Resizing(img_height, img_width),
        tf.keras.layers.Rescaling(1./255)  # Pixel vals to between 0 and 1
    ])
    data_augmentation = tf.keras.Sequential([  # Augmentation creates additional examples from the defined dataset
        tf.keras.layers.RandomFlip("horizontal_and_vertical"),
        tf.keras.layers.RandomRotation(0.2),
    ])

    # Start of Optimisation Features
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    # End of Optimisation Fetaures

    # Start of main model
    model = tf.keras.Sequential([
        resize_rescale,
        data_augmentation,
        tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes)
    ])
    # End of main model

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    return model, train_ds, val_ds, class_names

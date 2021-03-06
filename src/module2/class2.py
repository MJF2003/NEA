from pathlib import Path
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

# Defining constants
batch_size = 16
img_height = 100
img_width = 100
class_names = ['natspdlim', 'rdnarrows', 'thirtymph']


def build_model(dataset_loc: Path):
    """
    A very procedural function to assemble an ML model. Much of the code if referenced directly from the Tensorflow
    documentation. Defines datasets and the model including data augmentation
    :param dataset_loc: Location source of the data set.
    :return: Model object, Training and Validation datasets
    """
    try:
        # Extract Datasets from directory
        train_ds = tf.keras.utils.image_dataset_from_directory(  # Define the training set from the directory
            dataset_loc,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )
        val_ds = tf.keras.utils.image_dataset_from_directory(  # Same but for validation
            dataset_loc,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )


        my_classes = train_ds.class_names
        num_classes = len(my_classes)  # Number of possible classes the images could fall into

        resize_rescale = tf.keras.Sequential([  # Resizing the dataset components to square and correct size
            tf.keras.layers.Resizing(img_height, img_width),
            tf.keras.layers.Rescaling(1./255)  # Pixel vals to between 0 and 1
        ])
        data_augmentation = tf.keras.Sequential([  # Augmentation creates additional examples from the defined dataset
            tf.keras.layers.RandomFlip("horizontal_and_vertical"),
            tf.keras.layers.RandomRotation(0.2),
        ])

        # Start of Optimisation Features as described by tensorflow docs
        AUTOTUNE = tf.data.AUTOTUNE
        train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        # End of Optimisation Fetaures

        # Start of main model
        model = tf.keras.Sequential([
            resize_rescale,
            data_augmentation,

            tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(num_classes)
        ])
        # End of main model

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        return model, train_ds, val_ds
    except:
        print("Missing project dependencies. Ensure all are present")


def train(model, train_ds, val_ds, save_loc, epochs):
    """
    Trains the model built by the build_model() function
    :param model: Direct output of build model
    :param train_ds: Direct output of build model
    :param val_ds: Direct output of build model
    :param save_loc: Location to save the model to for further use
    :param epochs: Number of epochs to train on
    :return: None
    """
    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )
    model.save(save_loc)


def load_model(model_path: Path):
    """
    Loads the model specified by the path as a tf model object
    :param model_path: Location of weights folder
    :return: Model object
    """
    model = tf.keras.models.load_model(model_path)
    return model


def pred_img(array, model, lcl_classes):
    """
    Predicts the class of an unseen image using the softmax activation function
    :param array: Array containing image
    :param model: Model object
    :param lcl_classes: List of output classifications
    :return: The result of prediction attempt
    """
    predictions = model.predict(array)
    score = tf.nn.softmax(predictions[0])

    return score, f"""This image most likely belongs to {lcl_classes[np.argmax(score)]} 
        with a {100 * np.max(score):.2f} percent confidence."""

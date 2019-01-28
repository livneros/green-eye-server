import mnist
import numpy as np


def reshape_image_to_1D(image):
    return image.shape[0], image.shape[1] * image.shape[1]


def get_train_data():
    train_images = mnist.train_images()
    return train_images.reshape(reshape_image_to_1D(train_images))


def label(images, labels):
    labels = labels.reshape(labels.shape[0], 1)
    return np.concatenate((images, labels), axis=1)


def get_test_data():
    test_images = mnist.test_images()
    return test_images.reshape(reshape_image_to_1D(test_images))


def get_labels():
    train_labels = mnist.train_labels()
    test_labels = mnist.test_labels()
    return concatenate_data(train_labels, test_labels)


def get_data():
    train_images_labels = get_train_data()
    test_images_labels = get_test_data()
    return concatenate_data(test_images_labels, train_images_labels)


def concatenate_data(test_images_labels, train_images_labels):
    return np.concatenate((train_images_labels, test_images_labels))


def get_labeled_data():
    labeled_train_data = label(get_train_data(), mnist.train_labels())
    labeled_test_data = label(get_test_data(), mnist.test_labels())
    return concatenate_data(labeled_train_data, labeled_test_data)

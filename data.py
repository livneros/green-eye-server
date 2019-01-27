import mnist
import numpy as np

train_images = mnist.train_images()


def reshape(image):
    return (image.shape[0], image.shape[1] * image.shape[1])


train_images = train_images.reshape(reshape(train_images))
# images = train_images
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_images = test_images.reshape(reshape(test_images))
test_labels = mnist.test_labels()
images = np.concatenate((train_images, test_images))
# images = np.array([np.array([1, 2]), np.array([10, 20]), np.array([100, 200]),
#                    np.array([2, 3]), np.array([11, 21]), np.array([101, 201])])

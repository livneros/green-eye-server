import mnist

train_images = mnist.train_images()


def reshape_image_to_1D(image):
    return image.shape[0], image.shape[1] * image.shape[1]


train_images = train_images.reshape(reshape_image_to_1D(train_images))
images = train_images
# train_labels = mnist.train_labels()
# test_images = mnist.test_images()
# images = test_images.reshape(reshape_image_to_1D(test_images))
# test_images = test_images.reshape(reshape_image_to_1D(test_images))
# test_labels = mnist.test_labels()
# images = np.concatenate((train_images, test_images))

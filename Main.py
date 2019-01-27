import json

from sklearn.cluster import KMeans
from data import *
from PIL import Image

RGB = 'RGB'
MNIST_IMAGE_SIZE = 28
SAMPLES = "samples"
CENTERS = "centers"
IMAGES_PATH_ROOT = "static/images/"
SAMPLES_SIZE = 5


def get_samples(labels, label):
    return images[np.where(labels == label)][:SAMPLES_SIZE]


def run(n_clusters):
    kmeans = KMeans(n_clusters).fit(images)
    labels = kmeans.labels_
    samples = sample_from_each_label(labels, n_clusters)
    images_paths = {CENTERS: [], SAMPLES: []}
    save_centers(images_paths, kmeans)
    save_samples(images_paths, samples)
    return images_paths


def save_samples(images_paths, samples):
    j = 0
    for batch in samples:
        for i in range(SAMPLES_SIZE):
            image_name = 'sample-' + "digit=" + str(j) + "-" + str(i) + '.png'
            save_image(samples.get(batch)[i], image_name, images_paths, SAMPLES)
        j += 1


def save_centers(images_paths, kmeans):
    i = 0
    for center in kmeans.cluster_centers_:
        image_name = 'center' + str(i) + '.png'
        i += 1
        save_image(center, image_name, images_paths, CENTERS)


def save_image(image, image_name, images_paths, kind):
    im = Image.fromarray(np.array([image]).reshape((MNIST_IMAGE_SIZE, MNIST_IMAGE_SIZE))).convert(RGB)
    im.save(IMAGES_PATH_ROOT + image_name)
    images_paths.get(kind).append(image_name)


def sample_from_each_label(labels, n_clusters):
    samples = {}
    for label in range(n_clusters):
        samples[str(label)] = get_samples(labels, label)
    return samples
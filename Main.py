from PIL import Image

import kmeans_pre_processor
from mnist_pre_processor import *

RGB = 'RGB'
MNIST_IMAGE_SIZE = 28
SAMPLES = "samples"
CENTERS = "centers"
IMAGES_PATH_ROOT = "static/images/"
SAMPLES_SIZE = 5


def get_samples(samples, labels, label):
    return samples[np.where(labels == label)][:SAMPLES_SIZE]


def run(n_clusters):
    kmeans, labels, all_samples = kmeans_pre_processor.run_kmeans(n_clusters)
    samples = sample_from_each_label(labels, n_clusters)
    images_paths = {CENTERS: [], SAMPLES: {}}
    save_centers(images_paths, kmeans)
    save_samples(images_paths, samples)
    return images_paths


def save_samples(images_paths, samples):
    j = 0
    for label in range(len(samples.keys())):
        for i in range(min(SAMPLES_SIZE, len(samples.get(label)))):
            image_name = 'sample-' + "digit=" + str(j) + "-" + str(i) + '.png'
            save_image(samples.get(label)[i], image_name)
            if i == 0:
                images_paths.get(SAMPLES)[label] = []
            images_paths.get(SAMPLES).get(label).append(image_name)
        j += 1


def save_centers(images_paths, kmeans):
    i = 0
    for center in kmeans.cluster_centers_:
        image_name = 'center' + str(i) + '.png'
        i += 1
        save_image(center, image_name)
        images_paths.get(CENTERS).append(image_name)


def save_image(image, image_name):
    im = Image.fromarray(np.array([image]).reshape((MNIST_IMAGE_SIZE, MNIST_IMAGE_SIZE))).convert(RGB)
    im.save(IMAGES_PATH_ROOT + image_name)


def sample_from_each_label(all_samples, labels, n_clusters):
    samples = {}
    for label in range(n_clusters):
        samples[label] = get_samples(all_samples, labels, label)
    return samples

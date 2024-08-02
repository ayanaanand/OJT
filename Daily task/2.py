import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Define the data augmentation techniques
datagen = ImageDataGenerator(
    rotation_range=40,       # Randomly rotate images by up to 40 degrees
    width_shift_range=0.2,   # Randomly shift images horizontally by up to 20% of the width
    horizontal_flip=True     # Randomly flip images horizontally
)

# Load a sample image from TensorFlow datasets
(x_train, _), (_, _) = tf.keras.datasets.cifar10.load_data()
sample_image = x_train[0]  # Take the first image from the CIFAR-10 dataset
sample_image = sample_image.astype('float32') / 255.0  # Normalize the image
sample_image = sample_image.reshape((1,) + sample_image.shape)  # Reshape for the generator

# Generate augmented images and display them
plt.figure(figsize=(10, 10))
for i, batch in enumerate(datagen.flow(sample_image, batch_size=1)):
    if i >= 9:  # Generate 9 images
        break
    plt.subplot(3, 3, i + 1)
    img = batch[0]
    plt.imshow(img)
    plt.axis('off')

plt.show()

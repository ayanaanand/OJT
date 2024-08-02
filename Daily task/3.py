import tensorflow as tf
from tensorflow.keras import layers, models

# Define a custom loss function: MAE with L2 regularization
def custom_loss(y_true, y_pred):
    mae = tf.reduce_mean(tf.abs(y_true - y_pred))
    reg = 0.01 * tf.reduce_mean(tf.square(y_pred))  # L2 regularization
    return mae + reg

# Create a simple model
model = models.Sequential([
    layers.Dense(10, activation='relu', input_shape=(8,)),
    layers.Dense(1)
])

# Compile the model with the custom loss function
model.compile(optimizer='adam', loss=custom_loss)

# Example data
import numpy as np
x_train = np.random.random((100, 8))
y_train = np.random.random((100, 1))

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=10)

import os
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.applications import ResNet101
from tensorflow.keras.utils import image_dataset_from_directory



import time

img_height = 224
img_width = 224
batch_size = 32
epochs = 10
initial_learning_rate = 1e-5

data_dir = os.path.join(os.getcwd(), "train")

print("Zasoby:")
for device in tf.config.list_physical_devices():
    print(f" - {device.device_type}: {device.name}")

train_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    seed=42,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    shuffle=True,
)

val_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    seed=42,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    shuffle=False,
)

class_names = train_ds.class_names
num_classes = len(class_names)
print(f"\nWykryte klasy: {class_names}")

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.05),
    layers.RandomZoom(0.1)
])

train_ds = train_ds.map(lambda x, y: (data_augmentation(x / 255.0), tf.one_hot(y, num_classes)))
val_ds = val_ds.map(lambda x, y: ((x / 255.0), tf.one_hot(y, num_classes)))

train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=tf.data.AUTOTUNE)



base_model = ResNet101(
    include_top=False,
    weights='imagenet',
    input_shape=(img_height, img_width, 3),
    pooling='avg'
)
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

model = models.Sequential([
    base_model,
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(num_classes, activation='softmax')
])

model.compile(
    optimizer=optimizers.Adam(learning_rate=initial_learning_rate),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

start_time = time.time()

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

training_time = time.time() - start_time
print(f"\nCzas treningu: {training_time:.2f} sekund")

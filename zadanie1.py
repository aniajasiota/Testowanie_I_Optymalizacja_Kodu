#zadanie1

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = image.shape[:2]
center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Oryginalny obraz")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Obrócony obraz o 45 stopni")
plt.axis("off")

plt.show()

#zadanie8

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = image.shape[:2]
center = (width // 2, height // 2)

M_30 = cv2.getRotationMatrix2D(center, 30, 1)
rotated_image_30_1 = cv2.warpAffine(image, M_30, (width, height))
rotated_image_30_2 = cv2.warpAffine(rotated_image_30_1, M_30, (width, height))
rotated_image_30_3 = cv2.warpAffine(rotated_image_30_2, M_30, (width, height))

M_90 = cv2.getRotationMatrix2D(center, 90, 1)
rotated_image_90 = cv2.warpAffine(image, M_90, (width, height))

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.imshow(rotated_image_30_3)
plt.title("Obrót sekwencyjny o 3x30 stopni")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image_90)
plt.title("Obrót o 90 stopni")
plt.axis("off")

plt.show()

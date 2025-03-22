#zadanie7

import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = image.shape[:2]
center = (width // 2, height // 2)

M = cv2.getRotationMatrix2D(center, 60, 1)
rotated_image_cv2 = cv2.warpAffine(image, M, (width, height))

rotated_image_imutils = imutils.rotate(image, 60)

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.imshow(rotated_image_cv2)
plt.title("Obrót - cv2.warpAffine")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image_imutils)
plt.title("Obrót - imutils.rotate")
plt.axis("off")

plt.show()

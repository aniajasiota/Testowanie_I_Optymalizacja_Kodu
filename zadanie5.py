#zadanie5

import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

tx = int(input("Podaj przesunięcie w poziomie (tx): "))
ty = int(input("Podaj przesunięcie w pionie (ty): "))

shifted_image = imutils.translate(image, tx, ty)

height, width = image.shape[:2]
M = np.float32([[1, 0, tx], [0, 1, ty]])
warp_shifted_image = cv2.warpAffine(image, M, (width, height))

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Oryginalny obraz")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(shifted_image)
plt.title("Przesunięcie - imutils.translate")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(warp_shifted_image)
plt.title("Przesunięcie - cv2.warpAffine")
plt.axis("off")

plt.show()

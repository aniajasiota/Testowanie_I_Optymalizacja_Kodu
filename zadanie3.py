#zadanie3
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = image.shape[:2]

shift_x = width // 2 + 50
shift_y = height // 2 + 50

M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

shifted_image = cv2.warpAffine(image, M, (width, height))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Oryginalny obraz")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(shifted_image)
plt.title("Przesunięty obraz - duże przesunięcie")
plt.axis("off")

plt.show()

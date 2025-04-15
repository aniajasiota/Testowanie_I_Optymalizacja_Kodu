import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('6.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)

opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)
eroded = cv2.erode(closing, kernel, iterations=1)

titles = ['Oryginał', 'Progowanie', 'Po Otwarciu', 'Po Zamknięciu', 'Po Erozji']
images = [image, binary, opening, closing, eroded]

plt.figure(figsize=(12,6))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

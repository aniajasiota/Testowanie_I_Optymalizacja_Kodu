import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

erosion_square = cv2.erode(binary, kernel_square, iterations=1)
erosion_ellipse = cv2.erode(binary, kernel_ellipse, iterations=1)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(binary, cmap='gray')
plt.title("Oryginał")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(erosion_square, cmap='gray')
plt.title("Erozja – Kwadrat")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(erosion_ellipse, cmap='gray')
plt.title("Erozja – Elipsa")
plt.axis('off')

plt.tight_layout()
plt.show()

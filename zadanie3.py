import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('3.jpg', cv2.IMREAD_GRAYSCALE)

kernel_sizes = [3, 5, 7]
results = []

for k in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    results.append((k, opened))

plt.figure(figsize=(12, 4))
plt.subplot(1, len(kernel_sizes)+1, 1)
plt.imshow(image, cmap='gray')
plt.title("Oryginał")
plt.axis('off')

for idx, (k, img) in enumerate(results):
    plt.subplot(1, len(kernel_sizes)+1, idx+2)
    plt.imshow(img, cmap='gray')
    plt.title(f'Otwarcie k={k}')
    plt.axis('off')

plt.tight_layout()
plt.show()

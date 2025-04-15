import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel_sizes = [3, 5, 7]
iterations = [1, 2, 3, 4, 5]

fig, axs = plt.subplots(len(kernel_sizes), len(iterations) + 1, figsize=(15, 10))

for row_idx, kernel_size in enumerate(kernel_sizes):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))

    axs[row_idx, 0].imshow(binary, cmap='gray')
    axs[row_idx, 0].set_title(f'Original (k={kernel_size})')
    axs[row_idx, 0].axis('off')

    for col_idx, iteration in enumerate(iterations):
        dilated = cv2.dilate(binary, kernel, iterations=iteration)
        axs[row_idx, col_idx + 1].imshow(dilated, cmap='gray')
        axs[row_idx, col_idx + 1].set_title(f'Iteracja {iteration}')
        axs[row_idx, col_idx + 1].axis('off')

plt.tight_layout()
plt.show()

thicknesses = []

for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    object_thickness = []

    for iteration in iterations:
        dilated = cv2.dilate(binary, kernel, iterations=iteration)
        object_thickness.append(np.sum(dilated) / 255)

    thicknesses.append(object_thickness)

plt.figure(figsize=(8, 6))
for idx, thickness in enumerate(thicknesses):
    plt.plot(iterations, thickness, label=f'K={kernel_sizes[idx]}')

plt.xlabel('Liczba Iteracji')
plt.ylabel('Grubość Obiektów (suma pikseli)')
plt.title('Zmiana Grubości Obiektów w Zależności od Liczby Iteracji Dylatacji')
plt.legend()
plt.show()

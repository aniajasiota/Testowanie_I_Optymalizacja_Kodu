import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('4.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel_shapes = {
    'Prostokątny': cv2.MORPH_RECT,
    'Eliptyczny': cv2.MORPH_ELLIPSE
}

results = []

for name, shape in kernel_shapes.items():
    kernel = cv2.getStructuringElement(shape, (5, 5))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    results.append((name, closed))

plt.figure(figsize=(10, 4))
plt.subplot(1, len(results)+1, 1)
plt.imshow(binary, cmap='gray')
plt.title("Oryginał")
plt.axis('off')

for idx, (name, img) in enumerate(results):
    plt.subplot(1, len(results)+1, idx+2)
    plt.imshow(img, cmap='gray')
    plt.title(f'Zamknięcie\n{name}')
    plt.axis('off')

plt.tight_layout()
plt.show()

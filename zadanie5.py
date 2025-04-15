import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('5.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

shapes = {
    'Kwadrat': cv2.MORPH_RECT,
    'Krzyż': cv2.MORPH_CROSS,
    'Elipsa': cv2.MORPH_ELLIPSE
}

operations = {
    'Erozja': cv2.MORPH_ERODE,
    'Dylatacja': cv2.MORPH_DILATE,
    'Otwarcie': cv2.MORPH_OPEN,
    'Zamknięcie': cv2.MORPH_CLOSE,
    'Gradient': cv2.MORPH_GRADIENT
}

kernel_size = (5, 5)

fig, axs = plt.subplots(len(shapes), len(operations) + 1, figsize=(15, 8))

for row_idx, (shape_name, shape_type) in enumerate(shapes.items()):
    kernel = cv2.getStructuringElement(shape_type, kernel_size)

    axs[row_idx, 0].imshow(binary, cmap='gray')
    axs[row_idx, 0].set_title(f'Oryginał\n({shape_name})')
    axs[row_idx, 0].axis('off')

    for col_idx, (op_name, op_code) in enumerate(operations.items()):
        result = cv2.morphologyEx(binary, op_code, kernel)
        axs[row_idx, col_idx + 1].imshow(result, cmap='gray')
        axs[row_idx, col_idx + 1].set_title(op_name)
        axs[row_idx, col_idx + 1].axis('off')

plt.tight_layout()
plt.show()

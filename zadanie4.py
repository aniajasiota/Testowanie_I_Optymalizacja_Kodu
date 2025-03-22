#zadanie4

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = image.shape[:2]
center = (width // 2, height // 2)

angle = float(input('Podaj kąt obrotu: '))
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

plt.figure(figsize=(10, 5))
plt.imshow(rotated_image)
plt.title(f'Obrócony obraz o {angle} stopni')
plt.axis('off')
plt.show()

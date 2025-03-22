#zadanie3

import cv2
import numpy as np
import matplotlib.pyplot as plt

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width = image.shape[:2]
pivot = (0, 0)
rotation_matrix = cv2.getRotationMatrix2D(pivot, 30, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

plt.figure(figsize=(10, 5))
plt.imshow(rotated_image)
plt.title('Obrócony obraz o 30 stopni względem lewego górnego narożnika')
plt.axis('off')
plt.show()


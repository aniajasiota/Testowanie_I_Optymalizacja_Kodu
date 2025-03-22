#zadanie5
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rotated_image = imutils.rotate(image, 180)

plt.figure(figsize=(10, 5))
plt.imshow(rotated_image)
plt.title('Obrócony obraz o 180 stopni')
plt.axis('off')
plt.show()

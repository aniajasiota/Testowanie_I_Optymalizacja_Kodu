import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image.jpg")
B, G, R = cv2.split(image)

reordered = cv2.merge([R, B, G])
zero_G = cv2.merge([B, np.zeros_like(G), R])

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Oryginalny")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(reordered, cv2.COLOR_BGR2RGB))
plt.title("Kanały R-B-G")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(zero_G, cv2.COLOR_BGR2RGB))
plt.title("G = 0")
plt.axis("off")

plt.tight_layout()
plt.show()

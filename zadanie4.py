import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

b, g, r = cv2.split(image)

r_new = cv2.add(r, 30)
g_new = cv2.subtract(g, 20)
b_new = cv2.add(b, 10)

filtered = cv2.merge((b_new, g_new, r_new))
filtered_rgb = cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Oryginalny")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Filtr Instagram")
plt.imshow(filtered_rgb)
plt.axis("off")

plt.tight_layout()
plt.show()

import cv2
import matplotlib.pyplot as plt
import numpy as np

logo = cv2.imread("logo.png")
B, G, R = cv2.split(logo)

swapped = cv2.merge([R, G, B])
no_blue = cv2.merge([np.zeros_like(B), G, R])

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(logo, cv2.COLOR_BGR2RGB))
plt.title("Oryginalne logo")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(swapped, cv2.COLOR_BGR2RGB))
plt.title("Zamiana B ↔ R")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(no_blue, cv2.COLOR_BGR2RGB))
plt.title("Bez kanału B")
plt.axis("off")

plt.tight_layout()
plt.show()

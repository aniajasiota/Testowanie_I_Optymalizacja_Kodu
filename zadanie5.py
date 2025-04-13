import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("image.jpg")
M = np.float32([[1, 0, 10], [0, 1, 5]])
image2 = cv2.warpAffine(image1, M, (image1.shape[1], image1.shape[0]))

image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

diff = cv2.absdiff(image1, image2)
diff_rgb = cv2.cvtColor(diff, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Obraz 1 (oryginalny)")
plt.imshow(image1_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Obraz 2 (przesunięty)")
plt.imshow(image2_rgb)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Różnica (absdiff)")
plt.imshow(diff_rgb)
plt.axis("off")

plt.tight_layout()
plt.show()

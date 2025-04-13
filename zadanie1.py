import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

bright_numpy = image + 50
bright_numpy = np.clip(bright_numpy, 0, 255).astype(np.uint8)

bright_cv2 = cv2.add(image, np.ones(image.shape, dtype=np.uint8) * 50)

bright_numpy_rgb = cv2.cvtColor(bright_numpy, cv2.COLOR_BGR2RGB)
bright_cv2_rgb = cv2.cvtColor(bright_cv2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Oryginalny")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Jasność +50 (NumPy)")
plt.imshow(bright_numpy_rgb)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Jasność +50 (OpenCV)")
plt.imshow(bright_cv2_rgb)
plt.axis("off")

plt.tight_layout()
plt.show()

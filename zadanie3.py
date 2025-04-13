import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

dark_numpy = image - 80
dark_numpy = np.clip(dark_numpy, 0, 255).astype(np.uint8)

dark_cv2 = cv2.subtract(image, np.full(image.shape, 80, dtype=np.uint8))

dark_numpy_rgb = cv2.cvtColor(dark_numpy, cv2.COLOR_BGR2RGB)
dark_cv2_rgb = cv2.cvtColor(dark_cv2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Oryginalny")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Przyciemnienie (NumPy -80)")
plt.imshow(dark_numpy_rgb)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Przyciemnienie (cv2.subtract -80)")
plt.imshow(dark_cv2_rgb)
plt.axis("off")

plt.tight_layout()
plt.show()

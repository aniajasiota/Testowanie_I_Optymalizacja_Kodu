import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

burn_numpy = image + 150
burn_numpy = np.clip(burn_numpy, 0, 255).astype(np.uint8)

burn_cv2 = cv2.add(image, np.full(image.shape, 150, dtype=np.uint8))

burn_numpy_rgb = cv2.cvtColor(burn_numpy, cv2.COLOR_BGR2RGB)
burn_cv2_rgb = cv2.cvtColor(burn_cv2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Oryginalny")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Przepalenie (NumPy +150)")
plt.imshow(burn_numpy_rgb)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Przepalenie (cv2.add +150)")
plt.imshow(burn_cv2_rgb)
plt.axis("off")

plt.tight_layout()
plt.show()

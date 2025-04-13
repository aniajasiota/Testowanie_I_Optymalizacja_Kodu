import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

h, s, v = cv2.split(hsv)
s = cv2.add(s, 50, dst=s, mask=mask)
hsv_modified = cv2.merge([h, s, v])
result = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Oryginalny")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Zwiększone nasycenie czerwieni")
plt.axis("off")

plt.tight_layout()
plt.show()

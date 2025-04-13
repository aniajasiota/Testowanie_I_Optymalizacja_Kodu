import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
B, G, R = cv2.split(image)

R_boosted = cv2.add(R, 50)
boosted_image = cv2.merge([B, G, R_boosted])

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Oryginalny")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(boosted_image, cv2.COLOR_BGR2RGB))
plt.title("Wzmocniony kanał R")
plt.axis("off")

plt.tight_layout()
plt.show()

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
B, G, R = cv2.split(image)

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Oryginalny obraz')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(B, cmap='gray')
plt.title('Kanał B')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(G, cmap='gray')
plt.title('Kanał G')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(R, cmap='gray')
plt.title('Kanał R')
plt.axis('off')

plt.tight_layout()
plt.show()

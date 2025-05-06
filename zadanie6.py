import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (150, 100), (350, 300), 255, -1)

blurred = cv2.GaussianBlur(img_rgb, (25, 25), 0)

mask_3ch = cv2.merge([mask, mask, mask])
foreground = cv2.bitwise_and(img_rgb, mask_3ch)
background = cv2.bitwise_and(blurred, cv2.bitwise_not(mask_3ch))
combined = cv2.add(foreground, background)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Oryginalne zdjęcie")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(blurred)
plt.title("Całość rozmyta")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(combined)
plt.title("Efekt głębi ostrości")
plt.axis('off')
plt.tight_layout()
plt.show()

# === KOMENTARZE ===
# Ten efekt imituje małą głębię ostrości jak w aparatach z dużą przysłoną (np. f/1.8).
# GaussianBlur symuluje optyczne rozmycie tła, a ręczna maska pozwala zachować ostrość głównego obiektu.
# Lepsze rezultaty uzyskasz, jeśli maska precyzyjnie odwzorowuje sylwetkę obiektu (można to zrobić np. segmentacją).

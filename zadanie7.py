import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')

if image is None:
    raise FileNotFoundError("Nie znaleziono pliku image.jpg")

height, width, _ = image.shape
rows, cols = 3, 3
part_height = height // rows
part_width = width // cols

fig, axes = plt.subplots(rows, cols, figsize=(10, 10))
for i in range(rows):
    for j in range(cols):
        piece = image[i * part_height:(i + 1) * part_height, j * part_width:(j + 1) * part_width]
        axes[i, j].imshow(cv2.cvtColor(piece, cv2.COLOR_BGR2RGB))
        axes[i, j].axis('off')
plt.show()
import cv2
import matplotlib.pyplot as plt

image_path = "image.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Błąd: Nie można wczytać obrazu!")
else:
    flipped_both_axes = cv2.flip(image, -1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flipped_both_rgb = cv2.cvtColor(flipped_both_axes, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Oryginalny obraz")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(flipped_both_rgb)
    plt.title("Odbicie lustrzane względem obu osi")
    plt.axis("off")

    plt.show()

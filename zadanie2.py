import cv2
import matplotlib.pyplot as plt

image_path = "image.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Błąd: Nie można wczytać obrazu!")
else:
    flipped_vertical = cv2.flip(image, 0)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flipped_vertical_rgb = cv2.cvtColor(flipped_vertical, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Oryginalny obraz")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(flipped_vertical_rgb)
    plt.title("Odbicie lustrzane w pionie")
    plt.axis("off")

    plt.show()

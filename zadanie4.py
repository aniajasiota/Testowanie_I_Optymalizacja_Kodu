import cv2
import matplotlib.pyplot as plt

image_path = "image.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Błąd: Nie można wczytać obrazu!")
else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both_axes = cv2.flip(image, -1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flipped_horizontal_rgb = cv2.cvtColor(flipped_horizontal, cv2.COLOR_BGR2RGB)
    flipped_vertical_rgb = cv2.cvtColor(flipped_vertical, cv2.COLOR_BGR2RGB)
    flipped_both_rgb = cv2.cvtColor(flipped_both_axes, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Oryginalny obraz")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(flipped_horizontal_rgb)
    plt.title("Odbicie poziome")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(flipped_vertical_rgb)
    plt.title("Odbicie pionowe")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(flipped_both_rgb)
    plt.title("Odbicie względem obu osi")
    plt.axis("off")

    plt.show()

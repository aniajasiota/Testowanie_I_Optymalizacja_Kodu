import cv2
import matplotlib.pyplot as plt

image_path = "image.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Błąd: Nie można wczytać obrazu!")
else:
    height, width = image.shape[:2]
    right_half = image[:, width // 2:]

    flipped_right_half = cv2.flip(right_half, 1)

    image_with_flipped = image.copy()
    image_with_flipped[:, width // 2:] = flipped_right_half

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_with_flipped_rgb = cv2.cvtColor(image_with_flipped, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Oryginalny obraz")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(image_with_flipped_rgb)
    plt.title("Obraz po odbiciu na wybranym fragmencie")
    plt.axis("off")

    plt.show()

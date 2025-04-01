import cv2
import matplotlib.pyplot as plt

image_path = "image.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Błąd: Nie można wczytać obrazu!")
else:
    print("Wybierz typ odbicia:")
    print("0 – Odbicie pionowe")
    print("1 – Odbicie poziome")
    print("-1 – Odbicie względem obu osi")

    choice = int(input("Wprowadź swój wybór (0, 1, -1): "))

    if choice == 0:
        flipped_image = cv2.flip(image, 0)
    elif choice == 1:
        flipped_image = cv2.flip(image, 1)
    elif choice == -1:
        flipped_image = cv2.flip(image, -1)
    else:
        print("Błąd: Nieprawidłowy wybór!")
        exit()

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    flipped_rgb = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Oryginalny obraz")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(flipped_rgb)
    plt.title("Obraz po odbiciu")
    plt.axis("off")

    plt.show()

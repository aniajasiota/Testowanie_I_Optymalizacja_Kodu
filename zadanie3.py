import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def add_gaussian_noise(image, mean=0, std=25):
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

noisy_img = add_gaussian_noise(img)

params = [
    (5, 75, 75),
    (9, 100, 100),
    (15, 150, 150),
]

fig, axes = plt.subplots(len(params), 4, figsize=(18, 12))
fig.suptitle("Porównanie rozmyć – obraz z szumem", fontsize=18)

for i, (d, sigmaColor, sigmaSpace) in enumerate(params):
    # Bilateral
    bilateral = cv2.bilateralFilter(noisy_img, d, sigmaColor, sigmaSpace)

    gaussian = cv2.GaussianBlur(noisy_img, (9, 9), 0)

    median = cv2.medianBlur(noisy_img, 9)

    # Blur
    blur = cv2.blur(noisy_img, (9, 9))

    axes[i, 0].imshow(bilateral)
    axes[i, 0].set_title(f'Bilateral d={d}')
    axes[i, 1].imshow(gaussian)
    axes[i, 1].set_title('GaussianBlur')
    axes[i, 2].imshow(median)
    axes[i, 2].set_title('MedianBlur')
    axes[i, 3].imshow(blur)
    axes[i, 3].set_title('Average Blur')

for ax in axes.flatten():
    ax.axis('off')

plt.tight_layout()
plt.show()

# i. Czy rozmycie dwustronne skutecznie redukuje szum?
# -> Tak, rozmycie dwustronne bardzo dobrze tłumi szum, jednocześnie zachowując strukturę obrazu.
# -> Nie powoduje rozmycia krawędzi jak inne metody, nawet przy dużych wartościach parametrów.

# ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
# -> Tak. Rozmycie dwustronne działa przestrzennie i kolorystycznie – uwzględnia różnice intensywności,
#    dzięki czemu nie rozmywa ostrych krawędzi jak Gaussian czy Average blur.

# iii. Jakie wartości parametrów dają najlepsze rezultaty?
# -> Najlepszy kompromis (dla większości zdjęć): d=9, sigmaColor=100, sigmaSpace=100.
# -> Zbyt wysokie wartości mogą wygładzać zbyt mocno; zbyt niskie nie tłumią szumu wystarczająco.


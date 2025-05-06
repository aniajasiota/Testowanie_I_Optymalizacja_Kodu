import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def add_gaussian_noise(image, mean=0, std=25):
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy = cv2.add(image, noise)
    return noisy

def add_salt_pepper_noise(image, amount=0.02):
    noisy = image.copy()
    total_pixels = image.size // 3
    num_salt = int(amount * total_pixels)
    num_pepper = int(amount * total_pixels)

    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [255, 255, 255]

    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = [0, 0, 0]

    return noisy

noisy_gauss = add_gaussian_noise(img)
noisy_sp = add_salt_pepper_noise(img)

def apply_filters(noisy_img, ksize=5):
    results = {
        "Original + Noise": noisy_img,
        "Blur": cv2.blur(noisy_img, (ksize, ksize)),
        "Gaussian": cv2.GaussianBlur(noisy_img, (ksize, ksize), 0),
        "Median": cv2.medianBlur(noisy_img, ksize),
        "Bilateral": cv2.bilateralFilter(noisy_img, d=ksize, sigmaColor=75, sigmaSpace=75)
    }
    return results

filters_gauss = apply_filters(noisy_gauss)
filters_sp = apply_filters(noisy_sp)

def show_comparison(filters_dict, title):
    fig, axes = plt.subplots(1, len(filters_dict), figsize=(20, 5))
    fig.suptitle(title, fontsize=16)
    for ax, (name, img) in zip(axes, filters_dict.items()):
        ax.imshow(img)
        ax.set_title(name)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

show_comparison(filters_gauss, "Szum Gaussowski – porównanie metod rozmycia")
show_comparison(filters_sp, "Szum sól i pieprz – porównanie metod rozmycia")

# Szum Gaussowski:
# -> Najlepsze rezultaty: GaussianBlur i BilateralFilter.
# -> Gaussian usuwa szum gładko, Bilateral zachowuje więcej detali.

# Szum sól i pieprz:
# -> Najlepsze rezultaty: MedianBlur.
# -> Inne metody (Blur, Gaussian) mają słabe działanie — sól i pieprz pozostają widoczne.

# Wnioski:
# - **GaussianBlur**: najlepszy do szumu typu Gauss, szybki i skuteczny.
# - **MedianBlur**: idealny do szumu impulsowego (sól i pieprz).
# - **BilateralFilter**: bardzo dobre wyniki dla obu rodzajów, ale wolniejszy — najlepszy jeśli potrzebna jest jakość.
# - **cv2.blur**: najsłabszy — działa bardzo ogólnie, rozmywa wszystko, w tym krawędzie.

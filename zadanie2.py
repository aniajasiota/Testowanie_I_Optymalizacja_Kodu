import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel_sizes = [3, 5, 9, 15]

fig, axes = plt.subplots(len(kernel_sizes), 4, figsize=(16, 12))
fig.suptitle("Wpływ rozmiaru kernela na efekt rozmycia", fontsize=16)

for i, k in enumerate(kernel_sizes):
    blur = cv2.blur(img, (k, k))

    gaussian = cv2.GaussianBlur(img, (k, k), 0)

    median = cv2.medianBlur(img, k)

    bilateral = cv2.bilateralFilter(img, d=k, sigmaColor=75, sigmaSpace=75)

    axes[i, 0].imshow(blur)
    axes[i, 0].set_title(f'Blur (k={k})')
    axes[i, 1].imshow(gaussian)
    axes[i, 1].set_title(f'Gaussian (k={k})')
    axes[i, 2].imshow(median)
    axes[i, 2].set_title(f'Median (k={k})')
    axes[i, 3].imshow(bilateral)
    axes[i, 3].set_title(f'Bilateral (d={k})')

for ax in axes.flatten():
    ax.axis('off')

plt.tight_layout()
plt.show()

# i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
# -> Im większy kernel, tym mocniejsze rozmycie – obraz staje się bardziej "rozmyty" i traci detale.
# -> Przy dużych wartościach (np. 15x15), wiele szczegółów zostaje zatartych.
# -> Efekt jest najbardziej zauważalny przy blur i GaussianBlur. MedianBlur i bilateral są bardziej "odporne".

# ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
# -> Optymalny kompromis to kernel 5x5 lub 9x9, zależnie od rodzaju szumu:
#    - 5x5 dobrze usuwa lekki szum bez dużej utraty detali.
#    - 9x9 działa lepiej przy mocniejszym szumie, ale może nieco pogorszyć ostrość.
# -> Dla najlepszego balansu: **bilateral z k=9** lub **medianBlur z k=5/9**.


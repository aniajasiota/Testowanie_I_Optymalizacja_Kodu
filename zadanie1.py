import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel_sizes = [3, 5, 9]

fig, axes = plt.subplots(len(kernel_sizes), 4, figsize=(15, 10))
fig.suptitle("Porównanie metod rozmycia", fontsize=16)

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

# === KOMENTARZE ODPOWIADAJĄCE NA PYTANIA ===

# i. Która metoda najlepiej usuwa szum?
# -> Rozmycie medianowe najlepiej radzi sobie z usuwaniem szumu impulsowego (tzw. sól i pieprz).
# -> Rozmycie Gaussa dobrze tłumi szum gaussowski.
# -> Rozmycie dwustronne usuwa szum, ale zachowuje krawędzie – jest najbardziej zaawansowane.

# ii. Która metoda zachowuje najwięcej szczegółów?
# -> Rozmycie dwustronne najlepiej zachowuje szczegóły i krawędzie dzięki swojej naturze (przestrzenno-kolorowej filtracji).

# iii. Zalety i wady każdej metody:
# - cv2.blur:
#   + Zaleta: szybkie i proste.
#   - Wada: rozmywa wszystko, również krawędzie – słaba jakość.
# - cv2.GaussianBlur:
#   + Zaleta: lepsze niż zwykłe blur, mniej niszczy krawędzie.
#   - Wada: nadal może nie zachowywać dobrze detali.
# - cv2.medianBlur:
#   + Zaleta: świetne do usuwania szumu impulsowego.
#   - Wada: może deformować obraz przy dużych jądrach.
# - cv2.bilateralFilter:
#   + Zaleta: najlepsze do usuwania szumu przy zachowaniu krawędzi.
#   - Wada: wolniejsze, wymaga więcej zasobów obliczeniowych.
import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_text_image(text="TEST ROZMYCIA", width=400, height=150):
    img = np.ones((height, width, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, (10, height // 2), font, 1.5, (0, 0, 0), 3, cv2.LINE_AA)
    return img

text_img = create_text_image()

kernel_sizes = [5, 9, 15]

fig, axes = plt.subplots(len(kernel_sizes), 4, figsize=(18, 10))
fig.suptitle("Wpływ rozmycia na czytelność tekstu", fontsize=18)

for i, k in enumerate(kernel_sizes):
    blur = cv2.blur(text_img, (k, k))

    gaussian = cv2.GaussianBlur(text_img, (k, k), 0)

    median = cv2.medianBlur(text_img, k)

    bilateral = cv2.bilateralFilter(text_img, d=k, sigmaColor=75, sigmaSpace=75)

    axes[i, 0].imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
    axes[i, 0].set_title(f'Blur (k={k})')

    axes[i, 1].imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
    axes[i, 1].set_title(f'GaussianBlur (k={k})')

    axes[i, 2].imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB))
    axes[i, 2].set_title(f'MedianBlur (k={k})')

    axes[i, 3].imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB))
    axes[i, 3].set_title(f'Bilateral (d={k})')

for ax in axes.flatten():
    ax.axis('off')

plt.tight_layout()
plt.show()

# i. Które metody najmocniej rozmywają tekst?
# -> Najbardziej rozmywa tekst: cv2.blur i cv2.GaussianBlur przy dużych kernalach (np. 15x15).
# -> MedianBlur również może zniekształcać cienkie litery, zwłaszcza przy wysokich wartościach k.

# ii. Które pozwalają zachować jego czytelność?
# -> Najlepiej zachowuje tekst: cv2.bilateralFilter – nawet przy dużym d tekst pozostaje wyraźny.
# -> MedianBlur z k=5 lub 9 może być również akceptowalny, ale gorzej radzi sobie z cienkimi literami.


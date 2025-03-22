#zadanie 10

import cv2
import numpy as np

image = cv2.imread('image.jpg')

if image is None:
    print("Błąd: nie można wczytać obrazu. Sprawdź ścieżkę do pliku.")
    exit()

(h, w) = image.shape[:2]
cv2.imshow("Original", image)

if 50 >= h or 50 >= w or 200 >= h or 200 >= w:
    print("Błąd: współrzędne poza zakresem obrazu.")
    exit()

(b1, g1, r1) = image[50, 50].astype(int)
(b2, g2, r2) = image[200, 200].astype(int)

diff_r = abs(r1 - r2)
diff_g = abs(g1 - g2)
diff_b = abs(b1 - b2)

print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r1, g1, b1))
print("Pixel at (200, 200) - Red: {}, Green: {}, Blue: {}".format(r2, g2, b2))
print("Differences - Red: {}, Green: {}, Blue: {}".format(diff_r, diff_g, diff_b))

cv2.waitKey(0)
cv2.destroyAllWindows()

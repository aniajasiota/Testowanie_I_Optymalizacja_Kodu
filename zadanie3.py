#zadanie3

import cv2

image = cv2.imread('szare.jpg', cv2.IMREAD_GRAYSCALE)

if len(image.shape) == 2:
    num_channels = 1
else:
    num_channels = image.shape[2]

print(f"Liczba kanałów w obrazie: {num_channels}")

cv2.imshow("Obraz w odcieniach szarości", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

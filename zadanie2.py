import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

height = image.shape[0]
lower_half = image[height//2:]

cv2.imshow("Dolna połowa obrazu", lower_half)
cv2.waitKey(0)
cv2.destroyAllWindows()

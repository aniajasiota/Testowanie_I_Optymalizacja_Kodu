import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

width = image.shape[1]
right_half = image[:, width//2:]

cv2.imshow("Prawa połowa obrazu", right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()

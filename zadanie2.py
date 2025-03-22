#zadanie2

import cv2
image = cv2.imread('image.jpg')

num_channels = image.shape[2]

print(f"Liczba kanałów w obrazie: {num_channels}")

cv2.imshow("Kolorowy obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
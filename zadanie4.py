#zadanie4

import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)



x=int(input("Podaj wspolrzedna punktu X"))
y=int(input("Podaj wspolrzedna punktu Y"))

if 0 <= x < w and 0 <= y < h:
    image[y, x] = (0, 0, 0)
    print(f"Piksel na współrzędnych ({x}, {y}) został ustawiony na czarny.")
else:
    print("Błąd: Podane współrzędne wychodzą poza wymiary obrazu.")

cv2.imshow("Modified", image)
cv2.waitKey(0)
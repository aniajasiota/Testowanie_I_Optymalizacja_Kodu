import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

startX = int(input("Podaj współrzędną startX: "))
endX = int(input("Podaj współrzędną endX: "))
startY = int(input("Podaj współrzędną startY: "))
endY = int(input("Podaj współrzędną endY: "))

roi = image[startY:endY, startX:endX]

cv2.imshow("Wybrany ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

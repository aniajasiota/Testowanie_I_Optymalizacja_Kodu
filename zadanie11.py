#zadanie11
import cv2
import numpy as np

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

print("Brightest pixel at {} with intensity {}".format(maxLoc, maxVal))

cv2.waitKey(0)
cv2.destroyAllWindows()

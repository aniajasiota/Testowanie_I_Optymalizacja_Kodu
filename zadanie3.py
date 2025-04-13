import cv2
import numpy as np

img = cv2.imread("face.jpg")
img = cv2.resize(img, (400, 400))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Oryginal", img)
cv2.imshow("Maska (czerwony)", mask)
cv2.imshow("Tylko czerwony kolor", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

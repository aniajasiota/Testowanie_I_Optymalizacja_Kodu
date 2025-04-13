import cv2
import numpy as np

img = cv2.imread("face.jpg")
img = cv2.resize(img, (400, 400))

mask = np.zeros(img.shape[:2], dtype=np.uint8)
center = (200, 200)
axes = (100, 130)
cv2.ellipse(mask, center, axes, 0, 0, 360, 255, -1)

masked_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Oryginal", img)
cv2.imshow("Maska", mask)
cv2.imshow("Tylko twarz", masked_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

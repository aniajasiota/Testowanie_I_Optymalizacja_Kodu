import cv2
import numpy as np

img1 = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (400, 400))

M = np.float32([[1, 0, 5], [0, 1, 5]])
img2 = cv2.warpAffine(img1, M, (400, 400))

difference = cv2.bitwise_xor(img1, img2)

cv2.imshow("Obraz 1", img1)
cv2.imshow("Obraz 2 (przesuniety)", img2)
cv2.imshow("Roznice (XOR)", difference)

cv2.waitKey(0)
cv2.destroyAllWindows()

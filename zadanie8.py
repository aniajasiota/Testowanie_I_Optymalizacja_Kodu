import cv2
import numpy as np

image = cv2.imread("image.jpg")

height, width = image.shape[:2]
scale_factor = 4

cubic = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_CUBIC)
lanczos = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LANCZOS4)

comparison = np.hstack((cubic, lanczos))

cv2.imshow("INTER_CUBIC (lewo) vs INTER_LANCZOS4 (prawo)", comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()

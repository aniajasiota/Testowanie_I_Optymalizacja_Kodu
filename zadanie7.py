import cv2
import numpy as np

image = cv2.imread("image.jpg")

height, width = image.shape[:2]
scale_factor = 5

area = cv2.resize(image, (width // scale_factor, height // scale_factor), interpolation=cv2.INTER_AREA)
linear = cv2.resize(image, (width // scale_factor, height // scale_factor), interpolation=cv2.INTER_LINEAR)
cubic = cv2.resize(image, (width // scale_factor, height // scale_factor), interpolation=cv2.INTER_CUBIC)

comparison = np.hstack((area, linear, cubic))

cv2.imshow("Porównanie INTER_AREA vs inne", comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()

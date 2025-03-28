import cv2
import numpy as np

image = cv2.imread("image.jpg")

height, width = image.shape[:2]
scale_factor = 3

nearest = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_NEAREST)
linear = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)
cubic = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_CUBIC)
lanczos = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LANCZOS4)

comparison = np.hstack((nearest, linear, cubic, lanczos))

cv2.imshow("Porównanie interpolacji", comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()

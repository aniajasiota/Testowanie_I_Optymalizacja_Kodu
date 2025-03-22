#zadanie1
import cv2
import numpy as np

width, height = 400, 400
image = np.zeros((height, width, 3), dtype=np.uint8)

center = (width // 2, height // 2)

bottom_right = (width - 1, height - 1)

cv2.line(image, center, bottom_right, (255, 0, 0), 2)

cv2.imshow("Niebieska linia", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

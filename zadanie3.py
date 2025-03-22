#zadanie3
import cv2
import numpy as np

width, height = 300, 300
image = np.zeros((height, width, 3), dtype=np.uint8)

center_blue = (40, 40)
radius_blue = 40
cv2.circle(image, center_blue, radius_blue, (255, 0, 0), -1)

center_red = (width // 2, height // 2)
radius_red = 60
cv2.circle(image, center_red, radius_red, (0, 0, 255), -1)

cv2.imshow("Okręgi", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

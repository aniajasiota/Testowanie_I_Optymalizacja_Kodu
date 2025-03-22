#zadanie2
import cv2
import numpy as np

width, height = 400, 400
image = np.zeros((height, width, 3), dtype=np.uint8)

top_left_green = (0, 0)
bottom_right_green = (100, 50)
cv2.rectangle(image, top_left_green, bottom_right_green, (0, 255, 0), -1)

top_left_red = (300, 350)
bottom_right_red = (399, 399)
cv2.rectangle(image, top_left_red, bottom_right_red, (0, 0, 255), 3)

cv2.imshow("Prostokąty", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

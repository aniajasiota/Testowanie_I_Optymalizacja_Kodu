#zadanie4
import cv2
import numpy as np

width, height = 300, 300
image = np.zeros((height, width, 3), dtype=np.uint8)

center = (width // 2, height // 2)
top_left = (center[0] - 50, center[1] - 50)
bottom_right = (center[0] + 50, center[1] + 50)

cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), -1)
cv2.circle(image, center, 30, (255, 0, 0), -1)

cv2.imshow("Złożona figura", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

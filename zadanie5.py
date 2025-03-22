#zadanie5
import cv2
import numpy as np

width, height = 400, 400
image = np.zeros((height, width, 3), dtype=np.uint8)

center = (width // 2, height // 2)

for i in range(5):
    size = 20 + i * 20
    top_left = (center[0] - size // 2, center[1] - size // 2)
    bottom_right = (center[0] + size // 2, center[1] + size // 2)
    color = (0, 255 - i * 40, 255 - i * 40)
    cv2.rectangle(image, top_left, bottom_right, color, 2)

cv2.imshow("Kwadraty", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

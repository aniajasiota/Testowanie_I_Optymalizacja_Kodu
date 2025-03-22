#zadanie6

import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

center_x = w // 2
center_y = h // 2

half_size = 50
top_left_x = center_x - half_size
top_left_y = center_y - half_size
bottom_right_x = center_x + half_size
bottom_right_y = center_y + half_size

image[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = (0, 0, 255)

cv2.imshow("Modified", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

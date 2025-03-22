#zadanie7

import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]


part_h = h // 3
part_w = w // 3

center_fragment = image[part_h:2 * part_h, part_w:2 * part_w]

cv2.imshow("Original", image)

cv2.imshow("Center Fragment", center_fragment)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

width, height = 400, 400

triangle = np.zeros((height, width), dtype=np.uint8)
circle = np.zeros((height, width), dtype=np.uint8)

pts = np.array([
    [120, 300],
    [220, 300],
    [170, 200]
], np.int32)
cv2.fillPoly(triangle, [pts], 255)

cv2.circle(circle, (250, 250), 60, 255, -1)

and_img = cv2.bitwise_and(triangle, circle)
or_img = cv2.bitwise_or(triangle, circle)
xor_img = cv2.bitwise_xor(triangle, circle)
not_triangle = cv2.bitwise_not(triangle)

cv2.imshow("Trojkat", triangle)
cv2.imshow("Okrag", circle)
cv2.imshow("AND", and_img)
cv2.imshow("OR", or_img)
cv2.imshow("XOR", xor_img)
cv2.imshow("NOT Trojkat", not_triangle)

cv2.waitKey(0)
cv2.destroyAllWindows()

#zadanie9

import cv2

image = cv2.imread('image.jpg')

cv2.imshow("Original", image)

image[50:101, 50:101] = (255, 255, 255)

cv2.imshow("Modified", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

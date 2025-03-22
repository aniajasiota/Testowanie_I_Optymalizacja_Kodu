#zadanie9

import cv2
import numpy as np

image = cv2.imread('image.jpg')
height, width = image.shape[:2]
center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, 75, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imwrite('rotated_output.jpg', rotated_image)

#zadanie10
import cv2
import numpy as np

image = cv2.imread('image.jpg')
height, width = image.shape[:2]
center = (width // 2, height // 2)

for angle in range(0, 361, 15):
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    cv2.imshow('Obrót obrazu', rotated_image)
    cv2.waitKey(500)

cv2.destroyAllWindows()

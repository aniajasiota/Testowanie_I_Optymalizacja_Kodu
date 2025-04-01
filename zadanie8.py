import cv2
import numpy as np

image = cv2.imread('image.jpg')

if image is None:
    raise FileNotFoundError("Nie znaleziono pliku image.jpg")

height, width, _ = image.shape
roi_height, roi_width = 100, 100
step = 10

x_pos = 0
while True:
    roi = image[0:roi_height, x_pos:x_pos + roi_width]
    cv2.imshow("Przesuwający się ROI", roi)

    key = cv2.waitKey(0)
    if key == ord('q'):
        break

    x_pos += step
    if x_pos + roi_width > width:
        x_pos = 0

cv2.destroyAllWindows()

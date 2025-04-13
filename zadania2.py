import cv2
import numpy as np

img = cv2.imread("face.jpg")
img = cv2.resize(img, (400, 400))

masked_img = img.copy()
start_point = (120, 150)
end_point = (280, 190)
cv2.rectangle(masked_img, start_point, end_point, (0, 0, 0), -1)

cv2.imshow("Oryginal", img)
cv2.imshow("Zasloniete oczy", masked_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

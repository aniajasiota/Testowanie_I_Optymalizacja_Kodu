import cv2
import numpy as np

image = np.ones((200, 200, 3), dtype=np.uint8) * 255

roi = image[0:100, 0:100]

cv2.rectangle(image, (0, 0), (100, 100), (0, 255, 0), 2)

cv2.imshow("Obraz z zaznaczonym ROI", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
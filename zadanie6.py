#zadanie6
import cv2
import numpy as np

image = cv2.imread("profilowe.jpg")
image = cv2.resize(image, (900, 900))

face_center = (image.shape[1] // 2, image.shape[0] // 2)
face_radius = min(image.shape[0], image.shape[1]) // 3

eye_radius = 15
eye_y = face_center[1] - 30
eye_x1 = face_center[0] - 40
eye_x2 = face_center[0] + 40

mouth_top_left = (face_center[0] - 30, face_center[1] + 20)
mouth_bottom_right = (face_center[0] + 30, face_center[1] + 40)

cv2.circle(image, (eye_x1, eye_y), eye_radius, (0, 0, 255), -1)
cv2.circle(image, (eye_x2, eye_y), eye_radius, (0, 0, 255), -1)

cv2.rectangle(image, mouth_top_left, mouth_bottom_right, (0, 255, 0), -1)

cv2.circle(image, face_center, face_radius, (255, 0, 0), 3)

cv2.imshow("Zamazywanie szczegółów", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

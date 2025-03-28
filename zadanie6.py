import cv2
import imutils

image = cv2.imread("image.jpg")

resized_image = imutils.resize(image, height=400)

cv2.imshow("Obraz skalowany do 400px wysokości", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

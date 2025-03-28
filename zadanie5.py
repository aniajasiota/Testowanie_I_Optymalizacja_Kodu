import cv2
import imutils

image = cv2.imread("image.jpg")

resized_image = imutils.resize(image, width=500)

cv2.imshow("Obraz skalowany do 500px szerokości", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

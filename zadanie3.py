import cv2

image = cv2.imread("image.jpg")

resized_image = cv2.resize(image, (200, 300))

cv2.imshow("Obraz 200x300", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread("image.jpg")

height, width = image.shape[:2]

resized_image = cv2.resize(image, (width // 2, height // 2))

cv2.imshow("Zmniejszony obraz", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

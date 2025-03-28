import cv2

image = cv2.imread("image.jpg")

resized_image = cv2.resize(image, (800, int(image.shape[0] * 800 / image.shape[1])))

cv2.imwrite("resized_output.jpg", resized_image)

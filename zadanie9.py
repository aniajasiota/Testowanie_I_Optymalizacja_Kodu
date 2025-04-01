import cv2

image = cv2.imread('image.jpg')

if image is None:
    raise FileNotFoundError("Nie znaleziono pliku image.jpg")

height, width, _ = image.shape
crop_height, crop_width = 300, 300

cropped_image = image[0:crop_height, 0:crop_width]
cv2.imwrite('cropped_image.jpg', cropped_image)
import cv2

image = cv2.imread("image.jpg")

height, width = image.shape[:2]

for scale in range(100, 301, 20):
    resized_image = cv2.resize(image, (int(width * scale / 100), int(height * scale / 100)))
    cv2.imshow(f"Skalowanie: {scale}%", resized_image)
    cv2.waitKey(500)

cv2.destroyAllWindows()

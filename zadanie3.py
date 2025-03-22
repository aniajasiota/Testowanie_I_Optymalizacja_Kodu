#zadanie 3

import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

print((cX, cY))

(b, g, r) = image[400, 262]
print("Pixel at (400, 262) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


cv2.waitKey(0)
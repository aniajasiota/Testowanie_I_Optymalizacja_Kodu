#zadanie 4

import cv2

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imwrite('image_gray.jpg', image)

cv2.imshow("Obraz w skali szarości", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Obraz w skali szarości został zapisany jako 'image_gray.jpg'.")

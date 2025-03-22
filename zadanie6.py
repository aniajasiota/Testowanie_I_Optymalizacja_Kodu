#zadanie6
import cv2
image = cv2.imread('image.jpg')

cv2.namedWindow("Obraz", cv2.WINDOW_NORMAL)

cv2.imshow("Obraz", image)

cv2.resizeWindow("Obraz", 1800, 900)

cv2.waitKey(0)
cv2.destroyAllWindows()

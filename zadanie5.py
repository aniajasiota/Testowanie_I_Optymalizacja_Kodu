#zadanie5
import cv2

image1 = cv2.imread('image.jpg')
image2 = cv2.imread('szare.jpg')

cv2.imshow("Obraz 1", image1)
cv2.imshow("Obraz 2", image2)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

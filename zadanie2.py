#zadanie2
import cv2
image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# Modyfikacja piksela w prawym dolnym rogu na czerwony (0, 0, 255)
image[h-1, w-1] = (0, 0, 255)

# Wyświetlenie zmodyfikowanego obrazu
cv2.imshow("Modified", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

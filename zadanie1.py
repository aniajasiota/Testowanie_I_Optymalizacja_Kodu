import cv2

img = cv2.imread("image.jpg")
img = cv2.resize(img, (400, 400))

b, g, r = cv2.split(img)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

cv2.imwrite("blue_channel.jpg", b)
cv2.imwrite("green_channel.jpg", g)
cv2.imwrite("red_channel.jpg", r)

cv2.waitKey(0)
cv2.destroyAllWindows()

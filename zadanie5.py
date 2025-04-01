import cv2
import numpy as np

image = cv2.imread("face.jpg")

if image is None:
    print("Błąd: Nie można wczytać obrazu.")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) == 0:
    print("Błąd: Nie wykryto twarzy na obrazie.")
    exit()

(x, y, w, h) = faces[0]
face_roi = image[y:y+h, x:x+w]

cv2.imshow("Wykryta twarz", face_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

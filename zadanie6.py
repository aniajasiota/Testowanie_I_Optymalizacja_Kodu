import cv2

# Wczytanie obrazu
image = cv2.imread('image.jpg')

# Sprawdzanie czy obraz został poprawnie wczytany
if image is None:
    raise FileNotFoundError("Nie znaleziono pliku image.jpg")

# Przycinanie fragmentu obrazu o wymiarach 100x100 pikseli
x, y, w, h = 50, 50, 100, 100  # Pozycja x, y oraz szerokość i wysokość
fragment = image[y:y+h, x:x+w]

# Wklejanie fragmentu w nowe miejsce
image[200:200+h, 200:200+w] = fragment

# Zapisanie obrazu wynikowego
cv2.imwrite('result.jpg', image)
print("Obraz został zapisany jako result.jpg")

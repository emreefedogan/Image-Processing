import cv2
import numpy as np

def contra_harmonic_mean(img, size, Q):
    num = np.power(img, Q + 1)
    denom = np.power(img, Q)
    kernel = np.ones((size, size))
    result = cv2.filter2D(num, -1, kernel) / cv2.filter2D(denom, -1, kernel)
    result[denom == 0] = 0
    return result

img = cv2.imread('images/tuzbiber.png', cv2.IMREAD_GRAYSCALE)

# Kontra harmonik ortalama filtresi uygula
Q = 1 # Q > 0 tuz gürültüsünü, Q < 0 biber gürültüsünü azaltır
filtered = contra_harmonic_mean(img, 3, Q)

# Filtrelenmiş görüntüyü göster
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

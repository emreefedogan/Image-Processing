import cv2
import numpy as np
img = cv2.imread('images/icardi.png', cv2.IMREAD_GRAYSCALE)

# Doğrusal kontrast germe
min_val = np.min(img)
max_val = np.max(img)
linear_stretched = (img - min_val) / (max_val - min_val) * 255

# Kontrast germe
alpha = 1.5 # Kontrast seviyesi
beta = 0    # Parlaklık seviyesi
contrast_stretched = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# İşlenmiş görüntüleri göster
cv2.imshow('Orjinal Goruntu', img)
cv2.imshow('Doğrusal Germe', linear_stretched)
cv2.imshow('Kontrast Germe', contrast_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()

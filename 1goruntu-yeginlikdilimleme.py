import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('images/turk-parasi.png', cv2.IMREAD_GRAYSCALE)

# Yeğinlik seviyesi dilimlemesi için eşik değerlerini belirle
lower_threshold = 60
upper_threshold = 120

# Eşik değerlerine göre dilimleme yap
binary = np.zeros_like(img)
binary[(img > lower_threshold) & (img < upper_threshold)] = 255

# Dilimlenmiş görüntüyü göster
cv2.imshow('Orijinal Goruntu', img)
cv2.imshow('Dilimlenmis Goruntu', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

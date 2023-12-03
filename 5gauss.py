import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('images/turk-parasi.png')  # Türk parasının olduğu dosya adını gir

# Görüntüyü gri tonlamalıya dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Standart sapması 1 olan 5x5 Gauss filtresi oluştur
gaussian_kernel = cv2.getGaussianKernel(5, 1)
gaussian_filter = np.outer(gaussian_kernel, gaussian_kernel.transpose())

# Görüntüye Gauss filtresini uygula
filtered_image = cv2.filter2D(gray_image, -1, gaussian_filter)

# Sonuçları göster
cv2.imshow('Orijinal ', gray_image)
cv2.imshow('Gauss Filtreli Hali', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

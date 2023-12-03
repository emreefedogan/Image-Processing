import cv2
import numpy as np

# Resmi yerel dosyadan al
file_path = 'images/tuzbiber.png'
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # Resmi gri tonlamaya dönüştür

# Medyan filtresi
def median_filter(img, size):
    result = np.zeros_like(img, dtype=np.uint8)
    img = np.pad(img, (size // 2, size // 2), mode='constant')  # Sınır pikselleri için padding

    rows, cols = img.shape  # Görüntünün boyutlarını al

    for i in range(size // 2, rows - size // 2):
        for j in range(size // 2, cols - size // 2):
            neighbors = img[i - size // 2:i + size // 2 + 1, j - size // 2:j + size // 2 + 1].flatten()
            result[i - size // 2, j - size // 2] = np.median(neighbors)

    return result

# Ortalama filtresi
def mean_filter(img, size):
    result = np.zeros_like(img, dtype=np.uint8)
    img = np.pad(img, (size // 2, size // 2), mode='constant')  # Sınır pikselleri için padding

    rows, cols = img.shape  # Görüntünün boyutlarını al

    for i in range(size // 2, rows - size // 2):
        for j in range(size // 2, cols - size // 2):
            neighbors = img[i - size // 2:i + size // 2 + 1, j - size // 2:j + size // 2 + 1].flatten()
            result[i - size // 2, j - size // 2] = int(np.mean(neighbors))

    return result

# Görüntü boyutlarını kontrol et
if img is None:
    print(f"Resim yüklenemedi. Lütfen dosya yolunu kontrol edin: {file_path}")
    exit()

# Medyan ve Ortalama filtrelerini uygula
median_filtered_img = median_filter(img, size=5)  # Filtre boyutu ayarlanabilir
mean_filtered_img = mean_filter(img, size=5)  # Filtre boyutu ayarlanabilir

# Gürültülü ve filtrelenmiş resimleri göster
cv2.imshow('Gürültülü Resim', img)
cv2.imshow('Medyan Filtreli Resim', median_filtered_img)
cv2.imshow('Ortalama Filtreli Resim', mean_filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
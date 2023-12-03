import cv2
import numpy as np

img = cv2.imread('images/icardi.png', cv2.IMREAD_GRAYSCALE)

laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32)
laplacian_filtered = cv2.filter2D(img, -1, laplacian_kernel)

gauss_filtered = cv2.GaussianBlur(laplacian_filtered, (5, 5), 0)

cv2.imshow('Laplacian Filtered Image', laplacian_filtered)
cv2.imshow('Gauss Filtered Image', gauss_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

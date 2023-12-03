import cv2
import numpy as np

img = cv2.imread('images/icardi.png', cv2.IMREAD_GRAYSCALE)

box_size = 3
box_filter = np.ones((box_size, box_size), dtype = "float") * (1.0 / (box_size * box_size))
filtered = cv2.filter2D(img, -1, box_filter)
cv2.imshow('Orjinal Image', img)
cv2.imshow('Filtered Image', filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('images/icardi.png', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5),np.uint8)
max_filtered = cv2.dilate(img, kernel, iterations = 1)

box_size = 3
box_filter = np.ones((box_size, box_size), dtype = "float") * (1.0 / (box_size * box_size))
box_filtered = cv2.filter2D(img, -1, box_filter)

cv2.imshow('Max Filtered Image', max_filtered)
cv2.imshow('Box Filtered Image', box_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

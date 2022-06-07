import cv2
import numpy as np

image = cv2.imread('Fig1.tif')
kernel1 = np.ones((3,3), np.uint8)
kernel2 = np.ones((7,7), np.uint8)

dilation = cv2.dilate(image, kernel1, iterations = 8)
erosion = cv2.erode(dilation, kernel2, iterations = 3)

cv2.imshow('Input', image)
cv2.imshow('dilation', dilation)
cv2.imshow('erosion', erosion)
cv2.waitKey(0)
cv2.imwrite('./p1_d.jpg', dilation)
cv2.imwrite('./p1_e.jpg', erosion)
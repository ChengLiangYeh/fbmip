from PIL import Image
import numpy as np
import cv2

image = Image.open("Fig2.gif")
img = np.array(image)
print(img.shape)
print(img)  
threshold = input('please input a threshold  ')
threshold = int(threshold)

def thresholding(threshold, image):
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            if image[row][col] <= threshold:
                image[row][col] = 255
            else:
                image[row][col] = 0
    return image

afterT_img = thresholding(threshold, img)
cv2.imshow('afterT_img', afterT_img)
cv2.waitKey(0)
cv2.imwrite('./p2_a.jpg', afterT_img)  

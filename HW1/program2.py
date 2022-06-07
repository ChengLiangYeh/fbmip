import cv2
import numpy as np

img = cv2.imread('Fig1.bmp',cv2.IMREAD_GRAYSCALE)
print(img)
k = 8
while (k > 0):
    graylevels = 2**k
    print(graylevels)
    factor = 255 / graylevels
    reduced_image = np.uint8(np.floor(np.double(img)/255 * graylevels) * factor)
    print(reduced_image)
    cv2.imshow('img', reduced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    k = k - 1
    cv2.imwrite('program2_output_graylevel'+ str(graylevels) +'.png', reduced_image)
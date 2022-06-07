import cv2
import numpy as np

img = cv2.imread('Fig1.bmp',cv2.IMREAD_GRAYSCALE)
print(img.shape)
slide = 200
cv2.line(img, (150,150), (int(150-(slide/2)),int(150+(slide/2*(3**0.5)))), (255,255,255), 1)
cv2.line(img, (150,150), (int(150+(slide/2)),int(150+(slide/2*(3**0.5)))), (255,255,255), 1)
cv2.line(img, (int(150-(slide/2)),int(150+(slide/2*(3**0.5)))), (int(150+(slide/2)),int(150+(slide/2*(3**0.5)))), (255,255,255), 1)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('program1_output.png', img)

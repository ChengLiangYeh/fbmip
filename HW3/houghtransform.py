import cv2
import numpy as np
img = cv2.imread('p2_b.jpg')
output = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
detected_circles = np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0, :]:
    # draw the outer circle
    cv2.circle(output, (x,y), r, (0,255,0), 2)
    # draw the center of the circle
    cv2.circle(output, (x,y), 2, (0,255,255), 2)

cv2.imshow('output', output)
cv2.waitKey(0)
cv2.imwrite('./p2_c.jpg', output)  
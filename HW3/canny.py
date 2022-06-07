import cv2
image = cv2.imread('p2_a.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
canny = cv2.Canny(blurred, 70, 220) #
cv2.imshow('Input', image)
cv2.imshow('Result', canny)
cv2.waitKey(0)
cv2.imwrite('./p2_b.jpg', canny)  
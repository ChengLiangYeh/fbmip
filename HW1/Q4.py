from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = Image.open("Fig3.gif")
#img.show()
img.save('Fig3.png')

img = cv2.imread('Fig3.png', cv2.IMREAD_GRAYSCALE)
print(img.shape)

#畫histogram
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


'''
#gamma adjust
img = img / 255.0
gamma = 0.5
img = np.power(img, gamma)
cv2.imshow('Fig3_equal.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = img * 255
cv2.imwrite('Fig3_gamma.png', img)
'''


#clahe
#img = cv2.imread('Fig3_gamma.png', cv2.IMREAD_GRAYSCALE)
clahe = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('Fig3_gamma_clahe.png', cl1)
cv2.imshow('clahe.png', cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
#thresholding
for row in range(img.shape[0]):
    for column in range(img.shape[1]):
        grayvalue = img[row][column]
        if grayvalue > 207:
            img[row][column] = 255
        else:
            img[row][column] = 0
cv2.imshow('Fig3_equal.png', img)
cv2.waitKey(0)
'''


'''
#histogram equal
index = np.zeros([256])
for row in range(img.shape[0]):
    for column in range(img.shape[1]):
        grayvalue = img[row][column]
        index[grayvalue] = index[grayvalue] + 1
print(index)

cdf = np.zeros([256])
for i in range(256):
    if i == 0:
        cdf[i] = index[i]
        tem = index[i]
    else:
        tem = tem + index[i] 
        cdf[i] = tem

index_2 = np.zeros([256]) #轉換表: index是o~255 灰階 , value是指轉換後的灰階值

for i in range(256):
     index_2[i] = int(round(((cdf[i] - 1) / 195839) * 255))
print(index_2)

print(img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        value = img[i][j]
        img[i][j] = index_2[value]
print(img)

cv2.imwrite('Fig3_equal.png', img)
equal_img = cv2.imread('Fig3_equal.png')
cv2.imshow('Fig3_equal.png',equal_img)
cv2.waitKey(0)
'''
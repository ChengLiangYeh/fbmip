'''use library
from PIL import Image
img = Image.open('Fig2.bmp')
angle = 45
img_rotated = img.rotate(angle, resample=Image.NEAREST) 
img_rotated.show('img')
'''

#without powerful library 
import numpy as np
from PIL import Image
import math
from scipy import ndimage

img = ndimage.imread("Fig2.bmp")
#rotation_amount_degree = -90 #clockwise
rotation_amount_degree = input('please input rotation angle (- : clockwise)')
rotation_amount_degree = int(rotation_amount_degree)
rotation_amount_rad = rotation_amount_degree * np.pi / 180.0  #angle to radian

if len(img.shape) == 2:
    img2 = np.dstack((img, img))
    img = np.dstack((img2, img))
    print(img.shape)
height, width, num_channels = img.shape  #get image dimension

max_length = int(math.sqrt(height*height + width*width)) #最慘就45度
rotated_image = np.zeros((max_length, max_length, num_channels))

rotated_height, rotated_width, _ = rotated_image.shape
mid_row = int( (rotated_height+1)/2 )  #圖像正中心 row index
mid_col = int( (rotated_width+1)/2 )  #圖像正中心 col index
#mid_row = img.shape[0] / 2 
#mid_col = img.shape[1] / 2

#使用旋轉矩陣計算旋轉後的index
for r in range(rotated_height):
    for c in range(rotated_width):
        y = (r-mid_col)*math.cos(rotation_amount_rad) + (c-mid_row)*math.sin(rotation_amount_rad)
        x = -(r-mid_col)*math.sin(rotation_amount_rad) + (c-mid_row)*math.cos(rotation_amount_rad)
        y += mid_col -65 #offset, this number is test experience
        x += mid_row -130 #offset, this number is test experience
        #nearest neighbor interpolation
        x = round(x)
        y = round(y)
        if (x >= 0 and y >= 0 and x < width and y < height):
            rotated_image[r][c][:] = img[y][x][:]

#轉換data type後儲存
output_image = Image.fromarray(rotated_image.astype("uint8"))
output_image.save("rotated_image" + str(rotation_amount_degree) +".png")
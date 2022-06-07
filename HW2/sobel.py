import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

def Sobel(input_img_root):
    img = cv2.imread(input_img_root, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float64)
    shape = img.shape
    Gx = np.zeros([shape[0],shape[1]])
    Gy = np.zeros([shape[0],shape[1]])
    aftersobel_img = np.zeros([shape[0],shape[1]])
    
    for row in range(1,shape[0]-1):
        for col in range(1,shape[1]-1):
            s1 = (img[row-1][col-1] + (2*img[row][col-1]) + img[row+1][col-1]) - (img[row-1][col+1] + (2*img[row][col+1]) + img[row+1][col+1])
            s2 = (img[row-1][col-1] + (2*img[row-1][col]) + img[row-1][col+1]) - (img[row+1][col-1] + (2*img[row+1][col]) + img[row+1][col+1])

            if s1 > 255:
                s1 = 255
            elif s1 < 0:
                s1 = 0
            else:
                s1 = s1
            if s2 > 255:
                s2 = 255
            elif s2 < 0:
                s2 = 0
            else:
                s2 = s2
            
            Gy[row][col] = s1
            Gx[row][col] = s2
            aftersobel_img[row][col] = Gy[row][col] + Gx[row][col]
    Gy = Gy.astype('uint8')
    Gx = Gx.astype('uint8')
    aftersobel_img = aftersobel_img.astype('uint8')
    return Gy, Gx, aftersobel_img 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_img_root", help="input image root")
    parser.add_argument("--output_img_Gy_root", help="output Gy image after sobel  root")
    parser.add_argument("--output_img_Gx_root", help="output Gx image after sobel root")
    parser.add_argument("--output_img_afterSobel_root", help="output image after sobel root")
    augment = parser.parse_args()

    Gy, Gx, afterlaplacian_img = Sobel(augment.input_img_root)
    cv2.imwrite(augment.output_img_Gy_root, Gy)
    cv2.imwrite(augment.output_img_Gx_root, Gx)
    cv2.imwrite(augment.output_img_afterSobel_root, afterlaplacian_img)
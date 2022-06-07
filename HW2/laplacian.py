import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

def laplacian(input_img_root, output_img_root):
    img = cv2.imread(input_img_root, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float64)
    shape = img.shape
    afterlaplacian_img = np.zeros([shape[0],shape[1]])
    
    for row in range(1,shape[0]-1):
        for col in range(1,shape[1]-1):
            value = -img[row-1][col] - img[row+1][col] - img[row][col-1] - img[row][col+1] + (4 * img[row][col])
            if value > 255:
                value = 255
            elif value < 0:
                value = 0
            else:
                value = value
            afterlaplacian_img[row][col] = value
            
    afterlaplacian_img = afterlaplacian_img.astype('uint8')
    cv2.imwrite(output_img_root, afterlaplacian_img)
    return img, afterlaplacian_img

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_img_root", help="input image root")
    parser.add_argument("--output_img_afterLL_root", help="output image after laplacian root")
    parser.add_argument("--output_img_afterAdding_root", help="output image after Adding root")
    augment = parser.parse_args()
    img, afterlaplacian_img = laplacian(augment.input_img_root, augment.output_img_afterLL_root)
    C = img + afterlaplacian_img
    cv2.imwrite(augment.output_img_afterAdding_root, C)

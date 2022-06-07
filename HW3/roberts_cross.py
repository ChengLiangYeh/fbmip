import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse
import math

def Robert(input_img_root, output_img_root):
    img = cv2.imread(input_img_root, cv2.IMREAD_GRAYSCALE)
    shape = np.shape(img)
    new_img = np.zeros([shape[0],shape[1]])
    
    for row in range(shape[0]-1):
        for col in range(shape[1]-1):
            r1 = -1*(img[row][col]) + (img[row+1][col+1])
            r2 = -1*(img[row][col+1]) + (img[row+1][col])
            gradient = ((r1**(2)) + (r2**(2)))**(0.5)

            if gradient > 255:
                new_img[row][col] = 255
            elif gradient < 0:
                new_img[row][col] = 0
            else:
                new_img[row][col] = 255 - gradient #反白過來!
    new_img = new_img.astype('uint8')
    cv2.imwrite(output_img_root, new_img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_img_root", help="input image root")
    parser.add_argument("--output_img_root", help="output image root")
    augment = parser.parse_args()
    Robert(augment.input_img_root, augment.output_img_root)
import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse
import math

def average_filter(input_img_root, output_img_root, kernel_size):
    img = cv2.imread(input_img_root, cv2.IMREAD_GRAYSCALE)
    #print(type(img[0,0]))
    img = img.astype('float64')
    #print(type(img[0,0]))
    output = np.zeros([img.shape[0], img.shape[1]])
    #print(type(output[0,0]))

    for row in range(img.shape[0]-(kernel_size-1)):
        for col in range(img.shape[1]-(kernel_size-1)):
            #print(img[row:row+kernel_size, col:col+kernel_size])
            #print('================')
            #print(sum(( sum(img[row:row+kernel_size, col:col+kernel_size]) )))
            #print('================')
            #print(sum(( sum(img[row:row+kernel_size, col:col+kernel_size]) )) / (kernel_size**2))
            #print((row, col))
            #print(sum(( sum(img[row:row+kernel_size, col:col+kernel_size]) )) / (kernel_size**2))
            output[row, col]  = sum(( sum(img[row:row+kernel_size, col:col+kernel_size]) )) / (kernel_size**2)
    output = output.astype('uint8')
    cv2.imwrite(output_img_root, output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_img_root", help="input image root")
    parser.add_argument("--output_img_root", help="output image root")
    parser.add_argument("--kernel_size", type=int, help="kernel_size")
    augment = parser.parse_args()
    average_filter(augment.input_img_root, augment.output_img_root, augment.kernel_size)

    
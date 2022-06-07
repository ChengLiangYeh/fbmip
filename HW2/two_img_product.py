import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_img_A_root", help="input image A root")
parser.add_argument("--input_img_B_root", help="input image B root")
parser.add_argument("--output_img_root", help="output image root")
augment = parser.parse_args()

img_A = cv2.imread(augment.input_img_A_root, cv2.IMREAD_GRAYSCALE)
img_B = cv2.imread(augment.input_img_B_root, cv2.IMREAD_GRAYSCALE)
img_A = img_A.astype('float64')
img_B = img_B.astype('float64')
output = np.multiply(img_A, img_B) 

for row in range(output.shape[0]):
    for col in range(output.shape[1]):
        if output[row][col] > 255:
            output[row][col] = 255
        elif output[row][col] < 0:
            output[row][col] = 0

output = output.astype('uint8')
cv2.imwrite(augment.output_img_root, output)
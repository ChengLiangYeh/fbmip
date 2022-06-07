import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse
import math

def power_law(input_img_root, output_img_root, gamma):
    img = cv2.imread(input_img_root, cv2.IMREAD_GRAYSCALE)
    img = img.astype('float64')
    gamma_corrected_output = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
    cv2.imwrite(output_img_root, gamma_corrected_output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_img_root", help="input image root")
    parser.add_argument("--output_img_root", help="output image root")
    parser.add_argument("--gamma", type=float, help="gamma")
    augment = parser.parse_args()
    power_law(augment.input_img_root, augment.output_img_root, augment.gamma)

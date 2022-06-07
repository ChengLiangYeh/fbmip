import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

def plot_histogram(input_img_root, output_his_root):
    img = cv2.imread(input_img_root, cv2.IMREAD_GRAYSCALE)

    index = np.zeros([256]) #灰階 = 2**8
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            value = img[row][column]
            index[value] = index[value] + 1


    #plot histogram
    y_axis = index
    x_axis = np.zeros([256])
    for i in range(256):
        x_axis[i] = i

    plt.bar(x_axis, y_axis, width=1, linewidth=1)
    plt.xlabel("gray value")
    plt.ylabel("number")
    plt.title("histogram")
    plt.savefig(output_his_root)
    #plt.show()
    return img, index

def histogram_equalization(img, index, output_after_HE_img_root, output_after_HE_his_root):
    cdf = np.zeros([256])
    for i in range(256):
        if i == 0:
            cdf[i] = index[i]
            tem = index[i]
        else:
            tem = tem + index[i] 
            cdf[i] = tem          #累加!

    index_2 = np.zeros([256]) #轉換表: index是o~255 灰階 , value是指轉換後的灰階值
    for i in range(256):
        index_2[i] = int(round(((cdf[i] - 1) / (img.shape[0]*img.shape[1]-1) ) * 255))

    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            value = img[row][column]
            img[row][column] = index_2[value]

    cv2.imwrite(output_after_HE_img_root, img)
    img, index = plot_histogram(output_after_HE_img_root, output_after_HE_his_root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_img_root", help="input image root")
    parser.add_argument("--output_his_root", help="output histogram root")
    parser.add_argument("--output_after_HE_img_root", help="output after histogram equalization image root")
    parser.add_argument("--output_after_HE_his_root", help="output after histogram equalization histogrm root")
    augment = parser.parse_args()
    print(augment)
    img, index = plot_histogram(augment.input_img_root, augment.output_his_root)
    histogram_equalization(img, index, augment.output_after_HE_img_root, augment.output_after_HE_his_root)


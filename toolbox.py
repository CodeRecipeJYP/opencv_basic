from cv2 import *
import cv2
from matplotlib import pyplot as plt

def imshow_(img):
    imshow('jyp',img)
    waitKey(0)

def imshow_newtype(img):
    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.show()
    waitKey(0)

def adjustSobel(img):
    sobelx = Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    abs_grad_x = convertScaleAbs(sobelx)
    sobely = Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    abs_grad_y = convertScaleAbs(sobely)

    # laplacian = Laplacian(img, cv2.CV_64F)
    #
    # plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    # plt.title('Original'), plt.xticks([]), plt.yticks([])
    # plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    # plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    # plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    # plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    # plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    # plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    #
    # plt.show()

    grad = addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
#    imshow("Sobel Edge Detector", grad)


    return grad
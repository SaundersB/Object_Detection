import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt



def gather_images():
	return glob.glob('*.jpg')


def read_image():
	return cv2.imread('AlrmAV_12_14_44_272.jpg')


def display_image(img):
	if(img is not None):
		cv2.imshow('image', img) # Displays a GUI window of the image.
		cv2.waitKey(0) # Signals upon any keyboard key pressed.
		cv2.destoryAllWindows()

def plot_image(img):
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()


if __name__ == '__main__':
	print(gather_images())
	img = read_image()
	display_image(img)
	print(img.shape)
	print(img.size)
	print(img.dtype)
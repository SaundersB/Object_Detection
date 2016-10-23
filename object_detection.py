import cv2
import numpy as np
import glob



def gather_images():
	return glob.glob('*.jpg')


def read_image():
	return cv2.imread('AlrmAV_12_14_44_272.jpg')


def display_image(img):
	if(img is not None):
		cv2.imshow('image', img) # Displays a GUI window of the image.
		cv2.waitKey(0) # Signals upon any keyboard key pressed.
		cv2.destoryAllWindows()


if __name__ == '__main__':
	print(gather_images())
	img = read_image()
	display_image(img)
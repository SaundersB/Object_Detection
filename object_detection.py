import cv2
import numpy as np
import glob
import fnmatch
from matplotlib import pyplot as plt
import os


def obtain_path():
	return os.getcwd()

def gather_images():
	return glob.glob('*.jpg')

def find_files():
	# http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
	matches = []
	for root, dirnames, filenames in os.walk('images'):
	    for filename in fnmatch.filter(filenames, '*.jpg'):
	        matches.append(os.path.join(root, filename))
	return matches

def read_image():
	return cv2.imread('images/AlrmAV_12_14_44_272.jpg')


def display_image(img):
	if(img is not None):
		cv2.imshow('Image', img) # Displays a GUI window of the image.
		cv2.waitKey(0) # Signals upon any keyboard key pressed.
		cv2.destoryAllWindows()

def plot_image(img):
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()


if __name__ == '__main__':
	print(find_files())
	img = read_image()
	display_image(img)
	
import cv2
import numpy as np
import glob
import fnmatch
from matplotlib import pyplot as plt
import os
import time


def obtain_rtsp_stream():
	print("Obtaining RTSP stream...")
	video = cv2.VideoCapture("rtsp://username:password@IP_ADDRESS:PORT")
	print "Opened url"
	while(1):
		ret, frame = video.read()
		cv2.imshow('VIDEO', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break


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
		cv2.namedWindow("Image", cv2.IMREAD_COLOR) 
		cv2.imshow('Image', img) # Displays a GUI window of the image.
		cv2.waitKey(0) # Signals upon any keyboard key pressed.
		try:
			cv2.destoryAllWindows()
		except cv2.error as e:
			print(e)

def convert_to_grayscale(img):
	gray cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	laplacian = cv2.Laplacian(img,cv2.CV_64F)
	sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
	sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

	plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
	plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
	plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
	plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

	plt.show()


def plot_image(img):
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()


def capture_video():
	capture = cv2.VideoCapture(0)
	if not(capture.isOpened()):
		capture.open()
	time.sleep(5)
	capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
	capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
	capture.close()

if __name__ == '__main__':
	print(find_files())
	img = read_image()
	#display_image(img)
	convert_to_grayscale(img)
	#obtain_rtsp_stream()
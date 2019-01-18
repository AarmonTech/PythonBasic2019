#importing open cv library( Computer Vision)
import cv2
from time import sleep

#creating an instance of a camera on device
#with vriable named "cam"
#Integer in the VideoCapture(0) is index of the camera
#if you have 3 cameras on your system, you can access
#3rd camera with 2, 1s cmera with 0
cam = cv2.VideoCapture(0)
print(type(cam))

#Infinity Loop
while True:
	#now we read from the camera,
	#cam.read() returns, two values,
	#1st is status of image,either true or false
	#2nd is the actual image in form of array
	status , image = cam.read()

	#our Image is in form of numpy array
	#you can use print(image.shape) to know that it's a
	#3D array with 3rd axis as 3 values with R G B

	#we show the image on a window with imshow function from module cv2
	cv2.imshow("k.jpg",image)
	if cv2.waitKey(10) == ord("q"): #press q on window to exit the program
		break
	sleep(1/30)

#to write an image, we simple use imwrite("name_of_file.jpg",image)
cv2.imwrite("new.jpg",image)

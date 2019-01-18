import cv2
import cv2 as cv

from time import sleep

cam = cv2.VideoCapture(0)
print(cam.__class__)

status = True
while status:
	status , image = cam.read()

	#converting our image to Gray, ie black and white
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	thresh_1 = cv2.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)

	image = cv2.medianBlur(image,5)
	thresh_2 = cv2.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
	thresh_3 = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
	cv2.imshow("Thresh3",thresh_3)
	cv2.imshow("Thresh2",thresh_2)
	if cv2.waitKey(10) == ord("q"):
		break

	sleep(1/30)
else:
	print("Camera Faulty")

cv2.imwrite("new.jpg",image)

#using pillow library
from PIL import Image
import numpy as np

#opening the image in PIL.Image is simply open("file_name.jpg")
#or you can give full address as argument to  open()
image = Image.open("1.jpg")

#converting our image to numpy array
im_array = np.array(image)


print( im_array.shape )

#trying to crop a circle from the image, and leaving others black

#finding number of rows, and columns of our image array
row, col = im_array.shape[0], im_array.shape[1]
#center point of image
x , y =  row / 2, col / 2
image = im_array #for ease of use
#####################################################
#do something with image : im_array

""" #Foolish way of doing with numpy
for i in range(row):
	for j in range(col):
		#if lies outside of our rectanle , it's black else unchaanged
		if (i < (x - x/2)) or (i > (x + x/2)) or (j < (y - y/2)) or ( j > (y + y/2))
		
"""

#Better way of doingf the above with less cpu time
blank = np.zeros(image.shape,dtype=np.uint8)

blank[100:200,300:400] = image[100:200,300:400]
image = blank #overwriting variable image with blank, which is now a cropped image
######################################################


processed = Image.fromarray(image)

processed.save("croped.jpg")



"""
for i in range(row):
	for j in range(col):
		#if (i < ( row / 2 - row / 4)) or  ( i > ( row / 2 + row / 4)) or ( j > (col / 2 - 200)):
		if (i < row/4) or (i > row*3/4) or (j < col/4) or (j > col*3/4):
			image[i,j] = 0

"""
"""

"""
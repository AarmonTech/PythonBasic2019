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

#traversing through each pixel and making it black if needed
for i in range(row):
	for j in range(col):
		#if lies outside equation of circle, it's black else unchaanged
		if (x - i)**2 + (y - j)**2 > x**2:
			im_array[i,j] = 0

#converting back our numpy iamge array to PIL.Image format,
#so that our pillow image module can perform something
processed = Image.fromarray(im_array)

#in Pillow saving image to disk is simply save() which takes, name or full address as argument
processed.save("croped.jpg")

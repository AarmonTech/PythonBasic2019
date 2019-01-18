from PIL import Image
import numpy as np


image_2 = Image.open("2.jpg")
image_3 = Image.open("2.jpg")

im_array_2 = np.array(image_2)
im_array_3 = np.array(image_3)

print( im_array_2.shape, im_array_3.shape )


#do something with image : im_array
#here we are making steps of 20 in every color of the image.
im_array_2 = ( im_array_2 // 20 ) * 20


for i in range( im_array_3.shape[0] ):
	for j in range( im_array_3.shape[1] ):
		im_array_3[i][j] = im_array_3[i][j][0] // 3 + im_array_3[i][j][1] // 3 // 3 + im_array_3[i][j][2]  // 3


processed2 = Image.fromarray(im_array_2)

processed2.save("step_color_2.jpg")

processed3 = Image.fromarray(im_array_3)

processed3.save("grey_3.jpg")

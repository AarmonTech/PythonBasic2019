############################
#Numpy
#A numerical array library with various functions for
#operations, matrics, linear algebra,
#image processing, etc.
#Numpy is way way faster than any other data type in python
#it is more close to hardware than python variables,
#so its, very very fast
#and also very easy to do matrix and other mathematical computation
###########################

#import numpy with np as it's shorthand notation

import numpy as np

#create a numpy array as :

li = [1,2,3,56,23,78,34,67]
arr = np.array(li)

print("Dimension of array is : " , arr.ndim)

print("Shape of array(Matrix) is ", arr.shape)

print("Size of array is : ", arr.size)

#our current array is of one dimension only, but it can be of any dimension, 2, 3, 4,5 6 .....
arr_3_3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

##
#perform the above prints again on this array, and see the result
##

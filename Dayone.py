import numpy as np

array = [1,2,3,4,5]

array  = array*2
print(array)
print(type(array))
#<class 'list'> Type
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] List

array = np.array(array)
print(array)
print(type(array))
#<class 'numpy.ndarray'> Type
#[1 2 3 4 5 1 2 3 4 5] Array

array = array*2
print(array)
#[ 2  4  6  8 10  2  4  6  8 10]

brray = np.array([1,2,3,4,5,6,7,8,9,0])
print(array+brray)
#[ 3  6  9 12 15  8 11 14 17 10]
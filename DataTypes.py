import numpy as np

array = [1,2,3,4,5,6,7,8,9,0]
array = np.array(array)
print(array.dtype)
#dtype return the type of data being stored in the list or an array
#int64

array = np.array(array, dtype=np.int8)
print(array.dtype)
#dtype changed to int8

float = np.array([1.2,1.3,1.4,1.5,1.6])
print(float.dtype)
#float64

float = np.array(float, dtype=np.float16)
print(float.dtype)
#float16

float = np.array(float, dtype=np.str_)
print(float.dtype)
#<U32

float = np.array(float, dtype="<U5")
print(float.dtype)
#<U5    

object = np.array([1,1,'r',"dsfsf",True],dtype=np.object_)
print(object.dtype)
#object

array = array.astype(np.bool)
print(array.dtype)
#bool
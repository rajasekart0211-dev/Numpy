import numpy as np

arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [11,12,13,14]
])

print(arr[0])
# [1, 2, 3, 4]

print(arr[0][1])
# 2

print(arr[1:3]) #inclusive start: exclusive end 
#[[5, 6, 7, 8], [11, 12, 13, 14]]

print(arr[0:3:2]) #inclusive start: exclusive end : step  third argument start from the first element and jumps over the number of steps passed
#[[1, 2, 3, 4], [11, 12, 13, 14]]

print(arr[0:3:-1]) #-1 step willl reverse the matrix

print("slice")
print(arr[0:2:, 0:2:]) #slicing the columns with the , seperated value
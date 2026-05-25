import numpy as np

array = np.array(1)
print(array.ndim)
#0

one_dim_array = np.array([1,2,3,4,5,6,7,8])
print(one_dim_array.ndim)
#1

two_dim_array = np.array([
                        [1,2,3,4,5],
                        [5,6,7,8,9]
                          ])
print(two_dim_array.ndim)
#2

matrix = np.array([
    [
        [1,2,3,4,5],
        [6,7,8,9,0]
    ],
    [
        [5,4,3,2,1],
        [0,9,8,7,6]
    ]
])
print(matrix.ndim)
#3
print(matrix.shape)
#(2,2,5)

print(matrix)
#[[[1 2 3 4 5]
# [6 7 8 9 0]]
# [[5 4 3 2 1]
# [0 9 8 7 6]]]

matrix = matrix.reshape(2,10)
print(matrix)
#[[1 2 3 4 5 6 7 8 9 0]
#[5 4 3 2 1 0 9 8 7 6]]
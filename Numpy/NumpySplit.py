import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print("split 3 ",newarr)
newarr = np.array_split(arr, 5)
print("split 4 ",newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print("split 2D array ",newarr)

##Split 2D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print("split 2D array ",newarr)
##Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print("hsplit 2D array ",newarr)
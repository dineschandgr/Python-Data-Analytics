import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 1)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 1)
print(x)

##binary search
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
x = np.searchsorted(arr, 7, side='right')
print(x)
import numpy as np

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)

##gcd

num1 = 4
num2 = 6
x = np.gcd(num1, num2)
print(x)
arr = np.array([3, 6, 9])
x = np.gcd.reduce(arr)
print(x)
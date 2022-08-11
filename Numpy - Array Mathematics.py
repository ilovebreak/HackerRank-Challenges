import numpy as np
n, m = map(int, input().split())
arr1 = np.array([input().split() for _ in range(n)], int)
arr2 = np.array([input().split() for _ in range(n)], int)
print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.floor_divide(arr1, arr2))
print(np.mod(arr1, arr2))
print(np.power(arr1, arr2))

# Sample Input
# 1 4
# 1 2 3 4
# 5 6 7 8
# Sample Output
# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]] 
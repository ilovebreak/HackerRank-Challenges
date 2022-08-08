import numpy as np
np.set_printoptions(legacy='1.13')
arr = np.array(input().split(), float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

# Sample Input
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
# Sample Output
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
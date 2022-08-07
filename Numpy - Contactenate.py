import numpy as np
n, m, p = map(int, input().split())
arr1 = np.array([input().split() for _ in range(n)], int)
arr2 = np.array([input().split() for _ in range(m)], int)
print(np.concatenate((arr1, arr2), ))

# Sample Input

# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4 

# Sample Output

# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]] 

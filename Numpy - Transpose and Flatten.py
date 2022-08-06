import numpy
n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.transpose(arr))
print(arr.flatten())

# Sample Input
# 2 2
# 1 2
# 3 4
# Sample Output
# [[1 3]
#  [2 4]]
# [1 2 3 4]

# Sample Input
# 3 2
# 1 2
# 3 4
# 5 6
# Sample Output
# [[1 3 5]
# [2 4 6]]
# [1 2 3 4 5 6]
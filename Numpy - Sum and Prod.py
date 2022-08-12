import numpy
n, m = 2, 2 # map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(arr, axis = 0)))


# Sample Input
# 2 2
# 1 2
# 3 4
# Sample Output
# 24
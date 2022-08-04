import numpy
n, m = map(int, input().split())
my_list = []
for _ in range(n):
    my_list.append(input().split())
my_array = numpy.array(my_list, int)
print(my_array)
# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])
print(max(numpy.min(my_array, axis = 1)))

# хорошее объяснение:
# https://statisticsglobe.com/max-min-numpy-array-python

# Sample Input
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0
# Sample Output
# 3
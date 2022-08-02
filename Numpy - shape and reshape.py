from numpy import reshape
from numpy import array
# my_arr = array(("1 2 3 4 5 6 7 8 9").strip().split(' '), int)
# my_arr = array(input().strip().split(' '), int)
my_arr = array(input().split(), int)
print(reshape(my_arr, (3, 3)))

# Sample Input
# 1 2 3 4 5 6 7 8 9
# Sample Output
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
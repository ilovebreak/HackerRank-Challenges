from itertools import product
a, b = list(map(int, input().split())), list(map(int, input().split()))
for elem in list(product(a, b)):
    print(elem, end = " ")
    
# Sample Input
#  1 2
#  3 4
#  Sample Output
#   (1, 3) (1, 4) (2, 3) (2, 4)
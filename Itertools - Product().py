from itertools import product
a, b = list(map(int, input().split())), list(map(int, input().split()))
for elem in list(product(a, b)):
    print(elem, end = " ")

# Success!
from itertools import product
def sq(n):
    return n ** 2
iters, M = list(map(int, input().split()))
my_list = []
for i in range(iters):
    my_list.append(list(map(int, input().split()[1:])))
result = max(product(*my_list), key=lambda x: sum(list(map(sq,x))) % M)
print(sum(list(map(sq,result))) % M)
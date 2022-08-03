# x = 1
# y = 4
# exp = "x**3 + x**2 + x + 1"
# print(eval(exp))
# print(eval(exp) == y)

x, y = map(int, input().split())
exp = input()
print(eval(exp) == y)

# Sample Input
# 1 4
# x**3 + x**2 + x + 1
# Sample Output
# True
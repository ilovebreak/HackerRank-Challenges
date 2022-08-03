from collections import deque
d = deque()
n = int(input())
for i in range(n):
  user_cmd = input().split()
  try:
    eval(f'd.{user_cmd[0]}(int({user_cmd[1]}))')
  except:
    eval(f'd.{user_cmd[0]}()')
print(*d)

# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
# Sample Output
# 1 2
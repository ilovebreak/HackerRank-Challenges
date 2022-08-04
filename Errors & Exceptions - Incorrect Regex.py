import re

def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True
    
for i in range(int(input())):
    print(isvalidregex(input()))

# Sample Input
# 2
# .*\+
# .*+
# Sample Output
# True
# False
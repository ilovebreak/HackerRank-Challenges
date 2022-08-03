
from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
date1 = "Sun 10 May 2015 13:54:36 -0700"
date2 = "Sun 10 May 2015 13:54:36 -0000"

date1_fmt = dt.strptime(date1, fmt)
date2_fmt = dt.strptime(date2, fmt)
print(date1_fmt)
print(date2_fmt)
print((date1_fmt - date2_fmt).total_seconds())
print(abs(date1_fmt - date2_fmt).total_seconds())
print(int(abs(date1_fmt - date2_fmt).total_seconds()))

#Final short submission:
# for i in range(int(input())):
#     print(int(abs((dt.strptime(input(), fmt) - dt.strptime(input(), fmt)).total_seconds())))

# Sample Input 0
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0
# 25200
# 88200
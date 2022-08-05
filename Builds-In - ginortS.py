# #line = "Sorting1234"
# line = input()
# lowers = []
# uppers = []
# odds = []
# evens = []
# for letter in line:
#     if letter.isalpha() and letter.islower():
#         lowers.append(letter)
#     elif letter.isalpha() and letter.isupper():
#         uppers.append(letter)
#     elif letter.isnumeric() and int(letter) % 2 != 0:
#         odds.append(letter)
#     else:
#         evens.append(letter)
# print(*sorted(lowers), *sorted(uppers), *sorted(odds), *sorted(evens), sep = "")

#with regex:

import re
S= input()
series="[a-z]","[A-Z]","[13579]","[02468]"
print("".join(map(lambda x: "".join(sorted(re.findall(x, S))),series)))

# Sample Input
# Sorting1234
# Sample Output
# ginortS1324

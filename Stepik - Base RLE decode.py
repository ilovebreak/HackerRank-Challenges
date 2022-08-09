my_str = "3ab4c2CaB"
space_str = ''
result = ''
for letter in my_str:
    if letter.isnumeric():
        space_str += letter
    else:
        space_str += letter + " "
print(space_str)
space_list = space_str.split()
print(space_list)
for elem in space_list:
    if len(elem) == 1:
        result += elem
    else:
        print(elem[:-1])
        result += int(elem[:-1]) * elem[-1]
print(result)


# Sample Input:
# 3ab4c2CaB
# Sample Output:
# aaabccccCCaB
#line = "Sorting1234"
line = input()
lowers = []
uppers = []
odds = []
evens = []
for letter in line:
    if letter.isalpha() and letter.islower():
        lowers.append(letter)
    elif letter.isalpha() and letter.isupper():
        uppers.append(letter)
    elif letter.isnumeric() and int(letter) % 2 != 0:
        odds.append(letter)
    else:
        evens.append(letter)
print(*sorted(lowers), *sorted(uppers), *sorted(odds), *sorted(evens), sep = "")


# Sample Input
# Sorting1234
# Sample Output
# ginortS1324

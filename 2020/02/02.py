with open('input') as inputFile:
    data = inputFile.readlines()

valid_p1 = 0
valid_p2 = 0
for i in range(len(data)):
    strs = data[i].strip().split()
    low, high = [int(j) for j in strs[0].split('-')]
    char = strs[1][0]
    password = strs[2]

    # part 1
    count = password.count(char)
    if high >= count >= low:
        valid_p1 += 1

    #part 2
    if (password[low - 1] == char and password[high - 1] != char)\
            or (password[low - 1] != char and password[high - 1] == char):
        valid_p2 += 1

print(valid_p1)
print(valid_p2)

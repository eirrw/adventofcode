with open('input') as inputFile:
    data = inputFile.read()
    groups = data.split('\n\n')

sumYes = 0
for group in groups:
    users = [set(i) for i in group.split('\n')]
    maxYes = len(users[0].union(*users))

    sumYes += maxYes

print("Part 1: {}".format(sumYes))
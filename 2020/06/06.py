with open('input') as inputFile:
    data = inputFile.read()
    groups = data.split('\n\n')

sumAnyYes, sumAllYes = 0, 0
for group in groups:
    users = [set(i) for i in group.strip().split('\n')]
    anyYes = len(users[0].union(*users))
    allYes = len(users[0].intersection(*users))

    sumAnyYes += anyYes
    sumAllYes += allYes

print("Part 1: {}".format(sumAnyYes))
print("Part 2: {}".format(sumAllYes))

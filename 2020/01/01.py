with open('input') as inputFile:
    data = inputFile.readlines()
    data = [int(i) for i in data]

for i in data:
    sub = 2020 - i

    if sub in data:
        print("{} + {} = 2020".format(i, sub))
        print("{} * {} = {}".format(i, sub, i * sub))
        break

solved = False
for i in data:
    for j in data:
        if i == j:
            continue

        sub = 2020 - i - j
        if sub in data:
            print("{} + {} + {} = 2020".format(i, j, sub))
            print("{} * {} * {} = {}".format(i, j, sub, i*j*sub))
            solved = True
            break

    if solved:
        break
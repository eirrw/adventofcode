with open('input') as inputFile:
    data = inputFile.read().splitlines()

p1x, p1y = 3, 1
h = len(data)
w = len(data[0])


def run_map(xd, yd):
    x, y = 0, 0
    trees = 0
    while y < h:
        print("x: {}, y: {}".format(x, y))
        if data[y][x] == '#':
            trees += 1

        y += yd
        x += xd

        if x >= w:
            x = x - w

    return trees


print("part 1: {}".format(run_map(3, 1)))
p2 = run_map(1, 1) * run_map(3, 1) * run_map(5, 1) * run_map(7, 1) * run_map(1, 2)
print("part 2: {}".format(p2))

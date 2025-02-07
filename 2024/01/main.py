from collections import Counter

with open('input') as file:
    data = file.readlines()

list1 = []
list2 = []
for line in data:
    x, y = line.split()
    list1.append(int(x))
    list2.append(int(y))


def part1(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)

    if len(list1) != len(list2):
        raise IndexError

    dist = 0
    for x in range(len(list1)):
        dist += abs(list1[x] - list2[x])

    print(dist)


def part2(list1, list2):
    counts = Counter(list2)

    sim_score = 0
    for x in list1:
        c = counts[x]
        sim_score += x * c

    print(sim_score)


part1(list1, list2)
part2(list1, list2)

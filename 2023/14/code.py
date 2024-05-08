with open('input') as fp:
    platform = []
    for line in fp:
        platform.append(list(line.strip()))

cycles = 1000000000


def sort_platform(platform):
    for row in platform:
        start = 0
        rocks = row.count('O')  # get rocks
        i = 0
        while i < rocks:
            try:
                first_open = row.index('.', start)
            except ValueError:
                break

            first_cube = row.index('#', first_open) if '#' in row[first_open:] else len(row)

            if 'O' in row[first_open:first_cube]:
                first_rock = row.index('O', first_open, first_cube)
                row[first_open] = 'O'
                row[first_rock] = '.'
                i += 1
            else:
                start = first_cube+1


def run_cycle(platform):
    # north
    if cycle == 0:
        platform = list(reversed(list([*t] for t in zip(*platform))))
    else:
        platform = list([*t] for t in zip(*reversed(platform)))
    sort_platform(platform)

    # west
    platform = list([*t] for t in zip(*reversed(platform)))
    sort_platform(platform)

    # south
    platform = list([*t] for t in zip(*reversed(platform)))
    sort_platform(platform)

    # east
    platform = list([*t] for t in zip(*reversed(platform)))
    sort_platform(platform)

    return platform


repeats = []
for cycle in range(cycles):
    platform = run_cycle(platform)
    # for row in platform:
    #     print(' '.join(row))
    # print('\n')

    static_platform = tuple([tuple(x) for x in platform])

    if static_platform in repeats:
        index = repeats.index(static_platform)
        length = cycle - index
        offset = index + 1
        rem = (cycles - offset) % length

        print(f"Found repeat: {cycle}, {index}, {length}, {rem}, {offset}")

        for i in range(rem):
            platform = run_cycle(platform)
        break
    else:
        repeats.append(static_platform)


load = 0
for row in list([*t] for t in zip(*reversed(platform))):
    row_load = 0
    for k, v in enumerate(row):
        if v == 'O':
            row_load += len(row) - k

    load += row_load
    #print(' '.join(row), row_load)
print(load)

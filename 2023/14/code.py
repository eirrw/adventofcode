with open('input') as fp:
    platform = []
    for line in fp:
        platform.append(list(line.strip()))

#print(platform)

sorted_platform = []
for x in range(len(platform[0])):
    col = [platform[y][x] for y in range(len(platform))]
    #print(col)

    start = 0
    rocks = col.count('O')  # get rocks
    i = 0
    while i < rocks:
        try:
            first_open = col.index('.', start)
        except ValueError:
            break

        first_cube = col.index('#', first_open) if '#' in col[first_open:] else len(col)

        if 'O' in col[first_open:first_cube]:
            first_rock = col.index('O', first_open, first_cube)
            col[first_open] = 'O'
            col[first_rock] = '.'
            i += 1
        else:
            start = first_cube+1

    sorted_platform.append(col)

#print('finished')
load = 0
for row in sorted_platform:
    row_load = 0
    for k, v in enumerate(row):
        if v == 'O':
            row_load += len(row) - k

    load += row_load
    #print(row, row_load)

print(load)

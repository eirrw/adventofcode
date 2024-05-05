image = []
scale = 1000000

with open('input') as fp:
    for line in fp:
        row = list(line.strip())
        image.append(list(line.strip()))

rows = []
for row in image:
    if len(set(row)) == 1:
        rows.append(scale)
    else:
        rows.append(1)

cols = []
for x in range(len(image[0])):
    col = [image[i][x] for i in range(len(image))]
    if len(set(col)) == 1:
        cols.append(scale)
    else:
        cols.append(1)

# for row in image:
#     print(' '.join(row))
# print(rows)
# print(cols)

galaxy_locs = []
for y in range(len(image)):
    galaxy_locs.extend([(x, y) for x, g in enumerate(image[y]) if g == '#'])

print(galaxy_locs)

dist = 0
for i in range(len(galaxy_locs)):
    galaxy = galaxy_locs[i]

    for other in galaxy_locs[i+1:]:
        min_x = min(galaxy[0], other[0])
        max_x = max(galaxy[0], other[0])
        min_y = min(galaxy[1], other[1])
        max_y = max(galaxy[1], other[1])

        dist_x = sum(cols[min_x+1:max_x+1])

        dist_y = sum(rows[min_y+1:max_y+1])

#        print("{} -> {}: x{}, y{}, t{}".format(galaxy, other, dist_x, dist_y, dist_x+dist_y))

        dist += dist_x + dist_y


print(dist)

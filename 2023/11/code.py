image = []

with open('input') as fp:
    for line in fp:
        row = list(line.strip())

        # expand rows as we add them
        if len(set(row)) == 1 and '.' in row:
            image.append(list(line.strip()))
        image.append(list(line.strip()))

mirror_image = []
for x in range(len(image[0])):
    row = [image[i][x] for i in range(len(image))]
    if len(set(row)) == 1 and '.' in row:
        mirror_image.append(row)
    mirror_image.append(row)


for row in image:
    print(' '.join(row))
print()
for row in mirror_image:
    print(' '.join(row))

galaxy_locs = []
for y in range(len(mirror_image)):
    for x in range(len(mirror_image[y])):
        if mirror_image[y][x] == '#':
            galaxy_locs.append((x, y))

print(galaxy_locs)


dist = 0
for i in range(len(galaxy_locs)):
    galaxy = galaxy_locs[i]

    for other in galaxy_locs[i+1:]:
        dist_x = abs(galaxy[0] - other[0])
        dist_y = abs(galaxy[1] - other[1])
        print("{} -> {}: x{}, y{}, t{}".format(galaxy, other, dist_x, dist_y, dist_x+dist_y))

        dist += dist_x + dist_y


print(dist)

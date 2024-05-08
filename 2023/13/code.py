with open('input') as fp:
    data = fp.read()
    patterns = data.split('\n\n')


def count_mirrors(pattern, skip=None):
    count = 0
    for i in range(len(pattern)):
        valid = True
        x = i
        y = i+1
        if y < len(pattern) and pattern[x] == pattern[y] and (x, y) != skip:
            y += 1
            x -= 1

            while y < len(pattern) and x >= 0:
                if pattern[x] != pattern[y]:
                    valid = False
                    break
                y += 1
                x -= 1
        else:
            valid = False

        if valid:
            count = len(pattern[:i+1])
            break

    return (count, (i, i+1))


def matrix_print(matrix):
    for row in matrix:
        print(' '.join(row))


v_mirrors = {}
h_mirrors = {}
count_v = 0
count_h = 0
count_v2 = 0
count_h2 = 0
for k, v in enumerate(patterns):
    pattern = [list(x.strip()) for x in v.splitlines()]
    flipped_pattern = [[row[i] for row in pattern] for i in range(len(pattern[0]))]
    print(f"Pattern {k}")

    result = count_mirrors(pattern) # part 1
    if result[0]:
        count_h += result[0]
        h_mirrors[k] = result[1]
    else:
        result = count_mirrors(flipped_pattern)
        if result[0]:
            count_v += result[0]
            v_mirrors[k] = result[1]

    found = False
    for y, row in enumerate(pattern):
        for x, c in enumerate(row):
            pattern[y][x] = '.' if c == '#' else '#'

            result = count_mirrors(pattern, h_mirrors[k] if k in h_mirrors else None)
            if result[0]:
                print('found new horizontal mirror {}', result[1])
                count_h2 += result[0]
                found = True
                break

            pattern[y][x] = c
        if found:
            break

    if not found:
        for y, row in enumerate(flipped_pattern):
            for x, c in enumerate(row):
                flipped_pattern[y][x] = '.' if c == '#' else '#'

                result = count_mirrors(flipped_pattern, v_mirrors[k] if k in v_mirrors else None)
                if result[0]:
                    print('found new vertical mirror {}', result[1])
                    count_v2 += result[0]
                    found = True
                    break

                flipped_pattern[y][x] = c
            if found:
                break


print(count_v + (count_h * 100))
print(count_v2 + (count_h2 * 100))

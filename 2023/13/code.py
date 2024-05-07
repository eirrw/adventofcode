with open('input') as fp:
    data = fp.read()
    patterns = data.split('\n\n')


def count_mirrors(pattern):
    count = 0
    for i in range(len(pattern)):
        valid = True
        x = i
        y = i+1
        if y < len(pattern) and pattern[x] == pattern[y]:
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

    return count


count_v = 0
count_h = 0
for k, v in enumerate(patterns):
    pattern = [list(x.strip()) for x in v.splitlines()]

    count_h += count_mirrors(pattern)
    count_v += count_mirrors([[row[i] for row in pattern] for i in range(len(pattern[0]))])


print(count_v + (count_h * 100))


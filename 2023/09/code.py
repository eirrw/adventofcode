all_data = []


def get_diff(data):
    diffs = []
    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]
        diffs.append(diff)

    check = set(diffs)
    if len(check) == 1 and 0 in check:
        return 0

    new_diff = get_diff(diffs)
    return diffs[-1] + new_diff


with open('input') as fp:
    for line in fp:
        all_data.append([int(i) for i in line.strip().split()])

print(all_data)
data_sum = 0
for row in all_data:
    next_val = row[-1] + get_diff(row)
    data_sum += next_val

print(data_sum)

def get_diff(data, history=False):
    diffs = []
    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]
        diffs.append(diff)

    check = set(diffs)
    if len(check) == 1 and 0 in check:
        return 0

    new_diff = get_diff(diffs, history)
    if not history:
        return diffs[-1] + new_diff
    else:
        return diffs[0] - new_diff


all_data = []
with open('input') as fp:
    for line in fp:
        all_data.append([int(i) for i in line.strip().split()])

print(all_data)
data_sum = 0
prev_data_sum = 0
for row in all_data:
    next_val = row[-1] + get_diff(row)
    prev_val = row[0] - get_diff(row, True)
    data_sum += next_val
    prev_data_sum += prev_val

print(data_sum)
print(prev_data_sum)

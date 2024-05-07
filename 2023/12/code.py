from collections import namedtuple
from functools import cache

Record = namedtuple('Record', ['data', 'counts'])
scale = 5

records = []
with open('input') as fp:
    for line in fp:
        data = line.strip().split()
        print(data)
        records.append(Record('?'.join([data[0]]*scale), [int(i) for i in data[1].split(',')]*scale))

print(records)


@cache
def compute_arrangments(data, counts):
    if not counts:
        return 1 if '#' not in data else 0
    if not data:
        return 0

    result = 0
    if data[0] in '.?':
        result += compute_arrangments(data[1:], counts)
    if data[0] in '#?':
        if (
            counts[0] <= len(data)
            and '.' not in data[:counts[0]]
            and (len(data) == counts[0] or data[counts[0]] != '#')
        ):
            result += compute_arrangments(data[counts[0]+1:], counts[1:])

    return result


total_arrangements = 0
for record in records:
    print(f"Processing {record}")
    total_arrangements += compute_arrangments(record.data, tuple(record.counts))

print(total_arrangements)

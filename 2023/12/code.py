from collections import namedtuple
from itertools import product
import re

Record = namedtuple('Record', ['data', 'counts'])

records = []
with open('input') as fp:
    for line in fp:
        data = line.strip().split()
        records.append(Record(data[0], [int(i) for i in data[1].split(',')]))

print(records)

count_perms = 0
for record in records:
    count = record.data.count('?')
    print('Record: {}'.format(record))
    if count > 0:
        reps = product(['.', '#'], repeat=count)
        regex = r'^\.*' + r'\.+'.join([f"#{{{x}}}" for x in record.counts]) + r'\.*$'
        print(regex)

        for rep in reps:
            data = record.data
            for x in rep:
                data = data.replace('?', x, 1)

            if re.match(regex, data):
                count_perms += 1

            #print(data)

print(count_perms)

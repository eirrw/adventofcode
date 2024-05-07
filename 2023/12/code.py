from collections import namedtuple
from itertools import product
import re

Record = namedtuple('Record', ['data', 'counts'])

records = []
with open('example1') as fp:
    for line in fp:
        data = line.strip().split()
        print(data)
        records.append(Record('?'.join([data[0]]*5), [int(i) for i in data[1].split(',')]*5))

print(records)

count_perms = 0
for record in records:
    count = record.data.count('?')
    exist = record.data.count('#')
    print('Record: {}'.format(record))
    if count > 0:
        regex = r'^\.*' + r'\.+'.join([f"#{{{x}}}" for x in record.counts]) + r'\.*$'
        print(regex)

        for rep in product(['.', '#'], repeat=count):
            data = record.data
            for x in rep:
                data = data.replace('?', x, 1)
            if data.count('#') != sum(record.counts) - exist:
                continue

            if re.match(regex, data):
                count_perms += 1

            #print(data)

print(count_perms)

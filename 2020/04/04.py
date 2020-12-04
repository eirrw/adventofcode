import re

with open('input') as inputFile:
    data = inputFile.read().split('\n\n')

valid_passport = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

count = 0
for passport in data:
    fields = re.split(r'\s', passport)
    fields = [i[0:3] for i in fields]
    if set(fields).intersection(valid_passport) == set(valid_passport):
        count += 1

print("part 1: {}".format(count))

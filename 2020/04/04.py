import re

with open('input') as inputFile:
    data = inputFile.read().split('\n\n')

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_byr = range(1920, 2003)
valid_iyr = range(2010, 2021)
valid_eyr = range(2020, 2031)
valid_hgt = r'^([0-9]+)(in|cm)$'
valid_hgt_r = {
    'cm': range(150, 194),
    'in': range(59, 77)
}
valid_hcl = r'^#[0-9a-f]{6}$'
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid_pid = r'^[0-9]{9}$'

part1, part2 = 0, 0
for passport in data:
    fields = re.split(r'\s', passport.strip())
    fields = dict(i.split(':', 1) for i in fields)

    if set(fields.keys()).intersection(valid_fields) == set(valid_fields):
        part1 += 1
    else:
        continue

    if int(fields['byr']) not in valid_byr or \
            int(fields['iyr']) not in valid_iyr or \
            int(fields['eyr']) not in valid_eyr or \
            fields['ecl'] not in valid_ecl or \
            re.fullmatch(valid_hcl, fields['hcl']) is None or \
            re.fullmatch(valid_pid, fields['pid']) is None:
        continue

    hgt = re.fullmatch(valid_hgt, fields['hgt'])
    if hgt is None:
        continue
    else:
        n, t = hgt.groups()
        if int(n) not in valid_hgt_r[t]:
            continue

    part2 += 1

print("part 1: {}".format(part1))
print("part 2: {}".format(part2))

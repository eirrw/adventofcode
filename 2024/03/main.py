import re
from itertools import starmap
from operator import mul

with open('input') as file:
    data = file.read()

matches = re.findall(r"mul\((\d*),(\d*)\)", data)

print(sum(starmap(mul, [(int(x), int(y)) for x, y in matches])))

matches = re.findall(r"do(?:n't)?\(\)|mul\(\d*,\d*\)", data)
# print(matches)

add = True
tot = 0
for match in matches:
    if match == 'do()':
        add = True
    elif match == 'don\'t()':
        add = False
    elif add:
        nums = match.strip('mul()').split(',')
        tot += mul(int(nums[0]), int(nums[1]))

print(tot)

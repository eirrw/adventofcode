import re
from collections import namedtuple


def debug_print(string: str = '', should_print: bool = False):
    if should_print:
        print(string)


Gear = namedtuple('Gear', 'x y')

with open('input') as fp:
    lines = fp.read().splitlines()

debug = False
dim_x = len(lines[0])
dim_y = len(lines)
part_sum = 0
gears = {}
gear_sum = 0

for i, line in enumerate(lines):
    for match in re.finditer('[0-9]+', line):
        is_part = False
        debug_print('Match: {}'.format(match.group()), debug)

        for line_idx in range(max(i-1, 0), min(i+2, dim_y)):
            for char_idx in range(max(match.start() - 1, 0), min(match.end() + 1, dim_x)):
                char = lines[line_idx][char_idx]

                debug_print('Checking char at {},{}: {}'.format(char_idx, line_idx, char), debug)

                if char != '.' and not char.isdigit() and not is_part:
                    debug_print('Match is part', debug)
                    is_part = True
                else:
                    debug_print('Match is not part', debug)

                if char == '*':
                    debug_print('Is gear', debug)
                    gear = Gear(char_idx, line_idx)
                    if gear in gears.keys():
                        gears[gear].append(match.group())
                    else:
                        gears[gear] = [match.group()]

                    debug_print(gears[gear], debug)

            if is_part:
                break

        if is_part:
            debug_print('Result: part', debug)
            part_sum += int(match.group())
        else:
            debug_print('Result: not part', debug)
        debug_print('', debug)

for gear in gears:
    adj_parts = gears[gear]
    if len(adj_parts) == 2:
        gear_sum += (int(adj_parts[0]) * int(adj_parts[1]))

print(part_sum)
debug_print(gears, debug)
print(gear_sum)

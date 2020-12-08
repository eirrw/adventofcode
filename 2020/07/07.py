from collections import namedtuple
import re
from typing import List, Set

Bag = namedtuple('Bag', ('name', 'count'))

with open('input') as inputFile:
    data = inputFile.readlines()

bagsRoster = {}
for rule in data:
    base, contents = [i.strip().lower() for i in re.split('bags contain', rule)]

    matches = re.findall(r"([0-9]+ .*?(?= bag))", contents)

    bagsRoster[base] = []
    for m in matches:
        count, name = m.split(' ', 1)
        bagsRoster[base].append(Bag(name, int(count)))


def can_store_bag(needle: str, bag: str, checked: Set) -> (bool, List):
    stored = bagsRoster[bag]
    checked.add(bag)
    if needle in [i.name for i in stored]:
        return True, checked
    else:
        for sub_bag in [i for i in stored if i not in checked]:
            can_store, new_checked = can_store_bag(needle, sub_bag.name, checked)
            checked = checked.union(new_checked)
            if can_store:
                return True, checked

    return False, checked


count = 0
has_checked = set()
for parent_bag in bagsRoster.keys():
    bag_can_store, has_checked = can_store_bag('shiny gold', parent_bag, has_checked)
    if bag_can_store:
        count += 1

print(count)

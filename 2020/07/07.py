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


def can_store_bag(needle: str, parent_bag: str, checked: Set) -> (bool, List):
    stored = bagsRoster[parent_bag]
    checked.add(parent_bag)
    if needle in [i.name for i in stored]:
        return True, checked
    else:
        for child_bag in [i for i in stored if i not in checked]:
            can_store, new_checked = can_store_bag(needle, child_bag.name, checked)
            checked = checked.union(new_checked)
            if can_store:
                return True, checked

    return False, checked


def count_total_bags(parent_bag: str) -> int:
    total_bags = 0
    child_bags = bagsRoster.get(parent_bag)
    for child_bag in child_bags:
        total_bags += child_bag.count + (child_bag.count * count_total_bags(child_bag.name))

    return total_bags


count = 0
has_checked = set()
for bag in bagsRoster.keys():
    bag_can_store, has_checked = can_store_bag('shiny gold', bag, has_checked)
    if bag_can_store:
        count += 1

total = count_total_bags('shiny gold')


print("Part 1: {}".format(count))
print("Part 2: {}".format(total))


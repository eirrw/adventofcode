import re
from collections import namedtuple
from math import lcm
from functools import reduce

Node = namedtuple('Node', ['left', 'right'])

with open('input') as fp:
    # get directions
    dirs = fp.readline().strip()

    # skip line
    fp.readline()

    # get nodes
    nodes = {}
    for line in fp:
        m = re.match(r"^(.{3}) = \((.{3}), (.{3})\)$", line)
        nodes[m.group(1)] = Node(m.group(2), m.group(3))

cur_nodes = [n for n in nodes.keys() if n[-1] == 'A']
node_count = len(cur_nodes)
steps = 0
node_steps = []
found_exit = 0
while found_exit < node_count:
    for step in dirs:
        for n in range(len(cur_nodes)):
            if step == 'L':
                cur_nodes[n] = nodes[cur_nodes[n]].left
            elif step == 'R':
                cur_nodes[n] = nodes[cur_nodes[n]].right
            else:
                raise ValueError
        steps += 1

        for n in cur_nodes:
            if n[-1] == 'Z':
                found_exit += 1
                cur_nodes.remove(n)
                node_steps.append(steps)

print(reduce(lcm, node_steps))

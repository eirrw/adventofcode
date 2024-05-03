import re
from collections import namedtuple

Node = namedtuple('Node', ['left', 'right'])

with open('input') as fp:
    # get directions
    dirs = fp.readline().strip()

    # skip line
    fp.readline()

    # get nodes
    nodes = {}
    for line in fp:
        m = re.match(r"^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)$", line)
        nodes[m.group(1)] = Node(m.group(2), m.group(3))

cur_node = nodes['AAA']
steps = 0
last_nodes = []
found_exit = False
while True:
    for step in dirs:
        steps += 1
        if step == 'L':
            if cur_node.left == 'ZZZ':
                found_exit = True
                break
            cur_node = nodes[cur_node.left]
        elif step == 'R':
            if cur_node.right == 'ZZZ':
                found_exit = True
                break
            cur_node = nodes[cur_node.right]
        else:
            raise ValueError

    if found_exit:
        break

    if cur_node in last_nodes:
        print(last_nodes, cur_node, len(last_nodes))
        raise RuntimeError
    last_nodes.append(cur_node)

print(steps)

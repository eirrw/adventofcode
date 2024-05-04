from math import inf


class Node():
    prev = None
    dist = inf
    _neighbors = None

    def __init__(self, pipe: str, x: int, y: int):
        self.pipe = pipe
        self.x = x
        self.y = y

    def __repr__(self):
        return "Node: <{},{}: {}>".format(self.x, self.y, self.pipe)

    def get_neighbors(self):
        if self._neighbors:
            return self._neighbors

        if self.pipe == '|':
            self._neighbors = [(self.x, self.y - 1), (self.x, self.y + 1)]
        elif self.pipe == '-':
            self._neighbors = [(self.x - 1, self.y), (self.x + 1, self.y)]
        elif self.pipe == 'L':
            self._neighbors = [(self.x, self.y - 1), (self.x + 1, self.y)]
        elif self.pipe == 'J':
            self._neighbors = [(self.x, self.y - 1), (self.x - 1, self.y)]
        elif self.pipe == '7':
            self._neighbors = [(self.x, self.y + 1), (self.x - 1, self.y)]
        elif self.pipe == 'F':
            self._neighbors = [(self.x, self.y + 1), (self.x + 1, self.y)]

        return self._neighbors


graph = []
queue = []
nodes = []

with open('input') as fp:
    lines = fp.read().splitlines()
    for y in range(len(lines)):
        graph.append([])
        line = lines[y].strip()
        for x in range(len(line)):
            pipe = line[x]
            node = Node(pipe, x, y)
            graph[y].append(node)
            if pipe != '.':
                queue.append(node)
                nodes.append(node)

                if pipe == 'S':
                    node.dist = 0
                    u, d, l, r = [False] * 4
                    if y - 1 >= 0 and lines[y-1][x] in '|F7':
                        u = True
                    if y + 1 < len(lines) and lines[y+1][x] in '|JL':
                        d = True
                    if x - 1 >= 0 and line[x-1] in '-FL':
                        l = True
                    if x + 1 < len(line) and line[x+1] in '-J7':
                        r = True

                    if u and d:
                        node.pipe = '|'
                    elif u and r:
                        node.pipe = 'L'
                    elif u and l:
                        node.pipe = 'J'
                    elif l and r:
                        node.pipe = '-'
                    elif d and l:
                        node.pipe = '7'
                    elif d and r:
                        node.pipe = 'F'

while queue:
    cur_node = min(queue, key=lambda node: node.dist)
    if cur_node.dist == inf:
        break

    queue.remove(cur_node)

    for x, y in cur_node.get_neighbors():
        node = graph[y][x]
        if node in queue:
            alt = cur_node.dist + 1
            if alt < node.dist:
                node.dist = alt
                node.prev = cur_node


loop_nodes = [n for n in nodes if n.dist != inf]
print(max(loop_nodes, key=lambda node: node.dist).dist)

area = 0
for y in range(len(graph)):
    for x in range(len(graph[y])):
        # for every point in the graph
        node = graph[y][x]
        if node in loop_nodes:
            continue

        vert_rays = [
            [graph[i][x] for i in range(y)],  # up
            [graph[i][x] for i in range(y+1, len(graph))],  # down
        ]
        horz_rays = [
            graph[y][:x],  # left
            graph[y][x+1:],  # right
        ]

        def proc_ray(ray, ign_pipe, inc_pipe):
            global loop_nodes

            intersections = 0
            last_pipe = '.'
            for node in ray:
                if node.pipe != ign_pipe and node in loop_nodes:
                    if node.pipe == inc_pipe:
                        intersections += 1
                    elif (
                        (node.pipe == 'F' and last_pipe == 'J')
                        or (node.pipe == 'J' and last_pipe == 'F')
                        or (node.pipe == 'L' and last_pipe == '7')
                        or (node.pipe == '7' and last_pipe == 'L')
                    ):
                        intersections += 1
                        last_pipe = '.'
                    elif (
                        (node.pipe == 'F' and last_pipe in '7L')
                        or (node.pipe == 'J' and last_pipe in '7L')
                        or (node.pipe == '7' and last_pipe in 'FJ')
                        or (node.pipe == 'L' and last_pipe in 'FJ')
                    ):
                        intersections += 2
                        last_pipe = '.'
                    else:
                        last_pipe = node.pipe

            if intersections == 0:
                return -1
            return intersections % 2

        found = False
        for ray in vert_rays:
            res = proc_ray(ray, '|', '-')
            if res == -1:
                continue
            else:
                if res == 1:
                    area += 1
                found = True
                break

        if not found:
            for ray in horz_rays:
                res = proc_ray(ray, '-', '|')
                if res == -1:
                    continue
                else:
                    if res == 1:
                        area += 1
                    break

print(area)

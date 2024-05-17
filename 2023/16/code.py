from enum import Enum, auto
from functools import cache
from typing import NamedTuple


class Direction(Enum):
    LEFT = 0
    UP = auto()
    RIGHT = auto()
    DOWN = auto()


class NodeFunc(Enum):
    MIRROR_FORE = '/'
    MIRROR_BACK = '\\'
    SPLIT_VERT = '|'
    SPLIT_HORZ = '-'
    EMPTY = '.'


class Node(NamedTuple):
    func: NodeFunc
    x: int
    y: int


def get_next_dir(direction: Direction, func: NodeFunc):
    if func == NodeFunc.MIRROR_FORE:
        if direction in (Direction.LEFT, Direction.RIGHT):
            return [Direction((direction.value + 1) % 4)]
        else:
            return [Direction((direction.value + 3) % 4)]
    elif func == NodeFunc.MIRROR_BACK:
        if direction in (Direction.LEFT, Direction.RIGHT):
            return [Direction((direction.value + 3) % 4)]
        else:
            return [Direction((direction.value + 1) % 4)]
    elif func == NodeFunc.SPLIT_VERT:
        if direction in (Direction.LEFT, Direction.RIGHT):
            return [Direction((direction.value + 1) % 4), Direction((direction.value + 3) % 4)]
        else:
            return [direction]
    elif func == NodeFunc.SPLIT_HORZ:
        if direction in (Direction.UP, Direction.DOWN):
            return [Direction((direction.value + 1) % 4), Direction((direction.value + 3) % 4)]
        else:
            return [direction]
    else:
        return [direction]


def find_next_coord(direction: Direction, node: Node):
    if direction == Direction.LEFT:
        return (node.x + 1, node.y)
    if direction == Direction.UP:
        return (node.x, node.y - 1)
    elif direction == Direction.RIGHT:
        return (node.x - 1, node.y)
    elif direction == Direction.DOWN:
        return (node.x, node.y + 1)


def proc_grid(start_dir: Direction, start_node: Node):
    global grid
    queue = [(start_dir, start_node)]
    energized = []
    visited = []
    while queue:
        visit = queue.pop(0)
        direction, node = visit

        if visit not in visited:
            visited.append(visit)

            if node not in energized:
                energized.append(node)

            next_dirs = get_next_dir(direction, node.func)
            next_coords = [find_next_coord(next_dir, node) for next_dir in next_dirs]
            for n, coord in enumerate(next_coords):
                if coord[0] >= 0 and coord[0] < len(grid[0]) and coord[1] >= 0 and coord[1] < len(grid):
                    #visited.append((next_dirs[n], node))
                    queue.append((next_dirs[n], grid[coord[1]][coord[0]]))

    return len(energized)


grid = []
with open('input') as fp:
    lines = fp.read().splitlines()
    for y, line in enumerate(lines):
        row = []
        for x, c in enumerate(line.strip()):
            row.append(Node(NodeFunc(c), x, y))
        grid.append(row)

#for y in range(len(grid)):
visited = []
energized = []
total = proc_grid(Direction.LEFT, grid[0][0])

print(total)

part2 = 0
for row in range(len(grid)):
    part2 = max(part2, proc_grid(Direction.LEFT, grid[row][0]), proc_grid(Direction.RIGHT, grid[row][-1]))

print(part2)

from collections import namedtuple

with open('input') as file:
    data = file.readlines()

Index = namedtuple('Index', ['i', 'j'])
matrix = [list(x.strip()) for x in data]

#print(matrix)
H = len(matrix)
L = len(matrix[0])
chars = 'XMAS'


def check_next(next_char: int, cur_idx: Index, direction: Index):
    next_idx = Index(cur_idx.i + direction.i, cur_idx.j + direction.j)
    if next_idx.i >= 0 and next_idx.i < H and next_idx.j >= 0 and next_idx.j < L:
        if matrix[next_idx.i][next_idx.j] == chars[next_char]:
            #print("--> found {}, checking ({}, {})".format(chars[next_char], next_idx.i, next_idx.j))
            if chars[next_char] == chars[-1]:
                return True
            else:
                return check_next(next_char + 1, next_idx, direction)

    return False


count = 0
for i in range(H):
    for j in range(L):
        if matrix[i][j] == chars[0]:
            #print("found X at ({}, {})".format(i, j))
            for k in range(-1, 2):
                for l in range(-1, 2):
                    #print("-> checking ({}, {})".format(i+k, j+l))
                    if check_next(1, Index(i, j), Index(k, l)):
                        count += 1
print(count)

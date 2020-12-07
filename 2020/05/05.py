import math
import statistics

with open('input') as inputFile:
    data = inputFile.readlines()

ids = {}
for seat in data:
    rowStr = seat[0:7]
    colStr = seat[7:]

    rowVals = [0, 127]
    colVals = [0, 7]

    for i in rowStr:
        if i == 'F':
            rowVals[1] = math.floor(statistics.median(rowVals))
        else:
            rowVals[0] = math.ceil(statistics.median(rowVals))

    for i in colStr:
        if i == 'L':
            colVals[1] = math.floor(statistics.median(colVals))
        else:
            colVals[0] = math.ceil(statistics.median(colVals))

    rowId = rowVals[0] * 8
    if ids.get(rowId) is None:
        ids[rowId] = [colVals[0]]
    else:
        ids[rowId].append(colVals[0])

# p1
print("Part 1: {}".format(max(ids.keys()) + max(ids[max(ids.keys())])))

# p2
for k in ids.keys():
    if k != min(ids.keys()) and k != max(ids.keys()) and len(ids[k]) != 8:
        for l in range(0,8):
            if l not in ids[k]:
                print("Part 2: {}".format(k + l))

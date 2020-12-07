import math
import statistics

with open('input') as inputFile:
    data = inputFile.readlines()

maxId = 0
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

    if rowVals[0] != rowVals[1] or colVals[0] != colVals[1]:
        raise IndexError("Min and max does not match")

    id = rowVals[0] * 8 + colVals[0]
    maxId = max(maxId, id)

    print("row: {}, col: {}, id: {}".format(rowVals[0], colVals[0], id))

print(maxId)
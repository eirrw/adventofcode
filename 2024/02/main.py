from itertools import pairwise, starmap
from operator import lt, gt

with open('input') as file:
    data = file.readlines()

reports = []
for line in data:
    reports.append([int(x) for x in line.strip().split()])


def part1(reports):
    count = 0
    for report in reports:
        pairs = list(pairwise(report))
        if (all(starmap(lt, pairs)) or all(starmap(gt, pairs))) and all(abs(x - y) <= 3 for x, y in pairs):
            count += 1
      #       print(report, "safe")
      #   else:
      #       print(report, "unsafe")

    print(count)


def part2(reports):
    count = 0
    for report in reports:
        pairs = list(pairwise(report))

        asc = list(starmap(lt, pairs))
        desc = list(starmap(gt, pairs))
        dist = [abs(x - y) <= 3 for x, y in pairs]

        # print(report)
        # print(asc)
        # print(desc)
        # print(dist)
        if (all(asc) or all(desc)) and all(dist):
            count += 1
            # print("safe")
        else:
            idxs = []
            if False in asc and asc.count(True) > 1:
                idxs.append(asc.index(False))
            if False in desc and desc.count(True) > 1:
                idxs.append(desc.index(False))
            if False in dist:
                idxs.append(dist.index(False))

            if not idxs:
                # print("unsafe")
                continue

            idx = min(idxs)
#            print(asc, desc, dist, idxs)
            old = report.pop(idx)
            pairs = list(pairwise(report))
            if (
                (all(starmap(lt, pairs)) or all(starmap(gt, pairs)))
                and all(abs(x - y) <= 3 for x, y in pairs)
            ):
                count += 1
                # print("safe")
            else:
                report[idx] = old
                pairs = list(pairwise(report))
                if (
                    (all(starmap(lt, pairs)) or all(starmap(gt, pairs)))
                    and all(abs(x - y) <= 3 for x, y in pairs)
                ):
                    count += 1
                    # print("safe")
               # else:
                    # print("unsafe", idxs)
    print(count)


part1(reports)
part2(reports)

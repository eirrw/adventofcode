with open('input') as fp:
    times = [int(i) for i in fp.readline().strip().split()[1:]]
    recs = [int(i) for i in fp.readline().strip().split()[1:]]

prod = 1
for i in range(len(times)):
    print('Race {}: time {}, record {}'.format(i+1, times[i], recs[i]))
    wins = 0
    for x in range(times[i] + 1):
        time_rem = times[i] - x
        dist = x * time_rem

        win = False
        if dist > recs[i]:
            wins += 1
            win = True

        print('hold: {}, dist: {}, win: {}'.format(x, dist, win))

    print('wins: {}'.format(wins))
    prod *= wins

print('Total: {}'.format(prod))

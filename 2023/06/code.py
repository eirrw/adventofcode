with open('input') as fp:
    time = int(''.join(fp.readline().strip().split()[1:]))
    rec = int(''.join(fp.readline().strip().split()[1:]))

print('Race: time {}, record {}'.format(time, rec))
wins = 0
for x in range(time + 1):
    time_rem = time - x
    dist = x * time_rem

    win = False
    if dist > rec:
        wins += 1
        win = True

    #print('hold: {}, dist: {}, win: {}'.format(x, dist, win))

print('wins: {}'.format(wins))

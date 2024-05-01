import re

points = 0
total_cards = 0

reproc = []

with open('input') as fp:
    for game in fp:
        # print(reproc)
        repeat = reproc.pop(0) if len(reproc) > 0 else 0

        total_cards += 1 + repeat

        match = re.match(r"^Card\s+(?P<id>[0-9]+):(?P<winning>(?:\s+[0-9]{1,2})+) \|(?P<have>(?:\s*[0-9]{1,2})+)$", game)
        parsed = match.groupdict()

        winning_nums = parsed['winning'].strip().split()
        your_nums = parsed['have'].strip().split()
        # print(winning_nums, your_nums)

        # works if no duplicates
        count = len(set(winning_nums) & set(your_nums))
        # print(count)

        # part 1 - count points
        if count != 0:
            points += (2**(count-1))

        # part 2 - spawn new cards
        while True:
            for c in range(0, count):
                if c < len(reproc):
                    reproc[c] += 1
                else:
                    reproc.append(1)

            if repeat > 0:
                repeat -= 1
            else:
                break

    print(points)
    print(total_cards)

import re

points = 0

with open('input') as fp:
    for game in fp:
        match = re.match(r"^Card\s+(?P<id>[0-9]+):(?P<winning>(?:\s+[0-9]{1,2})+) \|(?P<have>(?:\s*[0-9]{1,2})+)$", game)

        parsed = match.groupdict()

        winning_nums = parsed['winning'].strip().split()
        your_nums = parsed['have'].strip().split()
        # print(winning_nums, your_nums)

        # works if no duplicates
        count = len(set(winning_nums) & set(your_nums))
        # print(count)

        if count != 0:
            points += (2**(count-1))

    print(points)

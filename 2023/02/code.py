import re
from collections import namedtuple

total_red = 12
total_green = 13
total_blue = 14

Game = namedtuple('Game', ['id', 'max_red', 'max_green', 'max_blue'])


def parse_game(game: str) -> Game:
    match = re.match(r"^Game (?P<id>[0-9]+)*:\s(?P<rounds>.*)$", game)
    matches = match.groupdict()
    id = matches['id']
    rounds = matches['rounds']

    max_red = 0
    max_green = 0
    max_blue = 0
    for round in rounds.split(';'):
        colours = re.findall("(?:([0-9]+) ((?:blue|green|red)))", round)
        for colour in colours:
            count = int(colour[0])

            if colour[1] == 'red' and count > max_red:
                max_red = count
            elif colour[1] == 'blue' and count > max_blue:
                max_blue = count
            elif colour[1] == 'green' and count > max_green:
                max_green = count

    return Game(id, max_red, max_green, max_blue)


with open('input') as fp:
    sum_ids = 0
    for game in fp:
        maxes = parse_game(game)
        valid = False

        if (
            maxes.max_red <= total_red
            and maxes.max_green <= total_green
            and maxes.max_blue <= total_blue
        ):
            valid = True
            sum_ids += int(maxes.id)

        print(game.strip())
        print(maxes)
        print(valid, '\n')

    print(sum_ids)

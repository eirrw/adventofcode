from bisect import bisect_left
from enum import Enum
from functools import total_ordering
from typing import Self


@total_ordering
class Type(Enum):
    FIVE = 7
    FOUR = 6
    FULL = 5
    THRE = 4
    TWOP = 3
    ONEP = 2
    HIGH = 1

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


def comp_cards(first, second):
    def assign_value(card):
        if card == 'A':
            return 14
        elif card == 'K':
            return 13
        elif card == 'Q':
            return 12
        elif card == 'J':
            return 11
        elif card == 'T':
            return 10
        elif card.isdigit():
            return int(card)
        else:
            raise ValueError

    val1 = assign_value(first)
    val2 = assign_value(second)

    if val1 == val2:
        return 0
    elif val1 > val2:
        return 1
    else:
        return -1


class Hand():
    type = None

    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid

    def __repr__(self):
        return "{} {} ({})".format(self.hand, self.bid, self.get_type())

    def get_type(self) -> Type:
        if self.type:
            return self.type

        uniques = {}
        for card in self.hand:
            count = uniques.setdefault(card, 0) + 1
            uniques[card] = count

        if len(uniques) == 5:
            self.type = Type.HIGH
        elif len(uniques) == 4:
            self.type = Type.ONEP
        elif len(uniques) == 3:
            if 2 in uniques.values():
                self.type = Type.TWOP
            else:
                self.type = Type.THRE
        elif len(uniques) == 2:
            if 3 in uniques.values():
                self.type = Type.FULL
            else:
                self.type = Type.FOUR
        elif len(uniques) == 1:
            self.type = Type.FIVE

        return self.type

    def __eq__(self, other: Self):
        if self.__class__ is other.__class__:
            if self.get_type() != other.get_type():
                return False

            for i in range(5):
                res = comp_cards(self.hand[i], other.hand[i])
                if res != 0:
                    return False

            return True
        return NotImplemented

    def __lt__(self, other: Self):
        if self.__class__ is other.__class__:
            if self.get_type() < other.get_type():
                return True
            elif self.get_type() > other.get_type():
                return False

            for i in range(5):
                res = comp_cards(self.hand[i], other.hand[i])
                if res == -1:
                    return True
                elif res == 1:
                    return False

            return False
        return NotImplemented


hands = []
with open('input') as fp:
    for line in fp:
        vals = line.strip().split()
        hand = Hand(vals[0], int(vals[1]))

        pos = bisect_left(hands, hand)
        hands.insert(pos, hand)

winnings = 0
for i in range(len(hands)):
    winnings += (i+1) * hands[i].bid

print(winnings)

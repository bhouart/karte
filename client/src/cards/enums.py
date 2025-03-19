from enum import Enum
class Rank(Enum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14


class Suit(Enum):
    hearts = 0
    diamonds = 1
    clubs = 2
    spades = 3
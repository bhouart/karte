from . import enums
class Card:
    def __init__(self, suit, rank):
        # Optionally convert integers to enum members if needed:
        self.suit = suit if isinstance(suit, enums.Suit) else enums.Suit(suit)
        self.rank = rank if isinstance(rank, enums.Rank) else enums.Rank(rank)

    def __repr__(self):
        return f"{self.rank.name.capitalize()} of {self.suit.name.capitalize()}"

    def __str__(self):
        return self.__repr__()

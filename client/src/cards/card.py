from . import enums
class Card:
    def __init__(self, suit, rank):
        # Optionally convert integers to enum members if needed:
        self.suit = suit if isinstance(suit, enums.Suit) else enums.Suit(suit)
        self.rank = rank if isinstance(rank, enums.Rank) else enums.Rank(rank)
    
    def __init__(self, id):
        suit = enums.Suit(id // 13)
        rank = enums.Rank(id % 13 + 2)
        self.__init__(suit, rank)

    def __repr__(self):
        return f"{self.rank.name.capitalize()} of {self.suit.name.capitalize()}"

    def __str__(self):
        return self.__repr__()

    def __lt__(self, other):
        return self.rank.value < other.rank.value
    def __le__(self, other):
        return self.rank.value <= other.rank.value
    def __eq__(self, other):
        return self.rank.value == other.rank.value
    def __ne__(self, other):
        return self.rank.value != other.rank.value
    def __gt__(self, other):
        return self.rank.value > other.rank.value
    def __ge__(self, other):
        return self.rank.value >= other.rank.value
        

    def get_id(self):
        return self.suit.value * 13 + self.rank.value - 2
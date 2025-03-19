from . import enums, card
from random import shuffle
class Deck:
    def __init__(self, cards=None):
        """
        :param cards: Optional list of Card objects. If not provided, a full deck is created.
        """
        self.cards = cards if cards is not None else []
        if not cards:
            self.__create_full_deck()
        
    def __create_full_deck(self):
        # Iterate directly over enum members.
        for rank in enums.Rank:
            for suit in enums.Suit:
                self.cards.append(card.Card(suit, rank))
    
    def shuffle(self):
        """Shuffles cards in the deck randomly."""
        shuffle(self.cards)
    
    def get_first(self):
        """Gets first card from the deck."""
        if self.cards:
            return self.cards.pop(0)
        return None
    
    def get_last(self):
        """Gets last card from the deck."""
        if self.cards:
            return self.cards.pop()
        return None

if __name__ == "__main__":
    deck = Deck()
    for card in deck.cards:
        print(card)
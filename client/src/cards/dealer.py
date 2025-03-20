from . import deck
class Dealer:
    def deal(self, master_deck, nbr_players):
        hands = [deck.Deck() for _ in range(nbr_players)]
        while master_deck.cards:
            for hand in hands:
                if master_deck.cards:  # Check if there are still cards to deal.
                    hand.cards.append(master_deck.get_first())
                else:
                    break
        return hands
    
    def shuffle(self,deck):
        deck.shuffle()
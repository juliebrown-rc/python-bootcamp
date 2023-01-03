from random import shuffle
from card import Card

class Deck():

    default_values = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    default_suits = 'clubs', 'spades', 'diamonds', 'hearts'

    def __init__(self, game_type='default'):
        self.draw_pile = []
        if game_type == 'default':
            for s in Deck.default_suits:
                for v in Deck.default_values:
                    self.draw_pile.append(Card(v, s, True))
    
    def shuffle_deck(self):
        self.draw_pile += self.discard_pile
        shuffle(self.draw_pile)

if __name__ == '__main__':
    new_deck = Deck()
    print(f"Built deck, {len(new_deck.draw_pile)} cards in draw_pile...")
    for c in new_deck.draw_pile:
        print(f"{c.label} of {c.suit}")

from random import shuffle
from card import Card

class Deck():

    default_values = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    default_suits = 'clubs', 'spades', 'diamonds', 'hearts'

    def __init__(self, game_type='default'):
        '''
        self.game_type always equals 'default' for now, preparing to support different deck configurations for other games
        self.draw_pile --> list of cards face down on the table
        self.discard_pile --> list of cards face up on the table, not used for war
        '''
        self.game_type = game_type
        self.draw_pile = []
        if game_type == 'default':
            for s in Deck.default_suits:
                for v in Deck.default_values:
                    self.draw_pile.append(Card(v, s, True))
        shuffle(self.draw_pile)

    def shuffle_deck(self):
        '''take all the cards from the discard pile back and shuffle'''
        self.draw_pile += self.discard_pile
        shuffle(self.draw_pile)

    def draw_card(self, player):
        '''take the last card in the draw pile and put it in a player's hand'''
        if len(self.draw_pile) == 0:
            print("No cards left in draw pile. Reshuffling.")
            self.shuffle_deck()
        new_card = self.draw_pile.pop()
        player.hand.append(new_card)

if __name__ == '__main__':
    # test creating a new deck of 52 cards
    new_deck = Deck()
    print(f"Built deck, {len(new_deck.draw_pile)} cards in draw_pile...")
    for c in new_deck.draw_pile:
        print(f"{c.label} of {c.suit}")

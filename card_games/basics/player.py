# import card

class Player():
    def __init__(self, name, hand=None):
        if hand is None:
            self.hand = []
        self.name = name
    
    def draw_card(self,deck):
        self.hand.append(deck.pop())
        return deck

    def print_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(f"{card.label} of {card.suit}")

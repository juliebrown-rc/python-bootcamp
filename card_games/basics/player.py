class Player():

    def __init__(self, name):
        '''
        player.name --> name of player
        player.hand --> list, contains card objects
        player.played_cards --> list, contains cards played on the table
        '''
        self.name = name
        self.hand = []
        self.played_cards = []

    def print_hand(self):
        '''print a list of all cards in hand'''
        print(f"\n{self.name}'s hand:")
        for card in self.hand:
            print(f"{card.label} of {card.suit}")

    def print_hand_length(self):
        '''print the number of cards in hand'''
        print(f"{self.name}: {len(self.hand)} cards")

    def has_cards(self):
        '''does this player have cards in their hand?'''
        return len(self.hand) > 0

    def play_card(self, card=None):
        '''play a card on the table, defaults to last card in list'''
        if card is None:
            card = self.hand.pop()
        else:
            self.hand -= [card]
        self.played_cards.append(card)
    
    def last_played_card(self):
        '''returns the last card played on the table'''
        return self.played_cards[-1]

    def pick_up_cards(self):
        '''pick up all of their played cards and add to the beginning of their hand'''
        while len(self.played_cards) > 0:
            self.hand.insert(0, self.played_cards.pop())
    
    def take_played_cards(self, player):
        '''pick up all of another player's played cards'''
        while len(player.played_cards) > 0:
            self.hand.insert(0, player.played_cards.pop())

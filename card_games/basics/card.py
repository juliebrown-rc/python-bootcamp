class Card():

    face_card_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    
    # TODO: Study field validations and make sure values are in acceptable ranges

    def __init__(self, label, suit, ace_high=False):
        '''
        card.label --> a string representing the card value ('A', '2', '3')
        card.value --> an int for card value. ace.value is 14 if ace_high=True, else ace.value=1
        card.suit --> 'clubs', 'hearts', 'diamonds', 'spades'
        '''
        self.label = str(label).upper()
        self.suit = suit
        try:
            self.value = int(self.label)
        except ValueError:
            self.value = Card.face_card_values[label]
            if self.label == 'A' and ace_high:
                self.value = 14

    def __str__(self):
        return f"{self.label} of {self.suit}"

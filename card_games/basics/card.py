class Card():

    face_card_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    
    def __init__(self, label, suit, ace_high=False):
        self.label = str(label).upper()
        self.suit = suit
        try:
            self.value = int(self.label)
        except ValueError:
            self.value = Card.face_card_values[label]
            if self.label == 'A' and ace_high:
                self.value = 14

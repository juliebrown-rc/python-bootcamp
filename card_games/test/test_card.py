import unittest

from basics.card import Card

# TODO: validations. check that suit is in a list of acceptable values

class Test_Card(unittest.TestCase):
    def test_new_card_middle_value(self):
        seven_card = Card(7, 'clubs')
        self.assertEqual(seven_card.value, 7)

    def test_face_card(self):
        king = Card('K', 'hearts')
        self.assertEqual(king.value, 13)
    
    def test_low_ace(self):
        low_ace = Card('A', 'spades', ace_high=False)
        self.assertEqual(low_ace.value, 1)
    
    def test_high_ace(self):
        high_ace = Card('A', 'diamonds', ace_high=True)
        self.assertEqual(high_ace.value, 14)


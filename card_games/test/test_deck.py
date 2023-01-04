import unittest

from basics.deck import Deck
from basics.player import Player

class Test_Deck(unittest.TestCase):
    def test_new_deck(self):
        new_deck = Deck()
        self.assertEqual(len(new_deck.draw_pile), 52)
    
    def test_draw_card(self):
        new_deck = Deck()
        new_player = Player('Jay')
        new_deck.draw_card(new_player)
        self.assertEqual(len(new_deck.draw_pile), 51)
        self.assertEqual(len(new_player.hand), 1)
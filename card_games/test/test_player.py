import unittest

from basics.card import Card
from basics.player import Player

class Test_Player(unittest.TestCase):
    def test_new_player(self):
        jay = Player('Jay')
        self.assertEqual(jay.name, 'Jay')
        self.assertEqual(jay.hand, [])
    
    def test_draw_card(self):
        ace = Card('A', 'clubs')
        jay = Player('Jay', None)
        jay.draw_card([ace])
        self.assertEqual(jay.hand, [ace])

import unittest
from basics.player import Player

class Test_Player(unittest.TestCase):
    def test_new_player(self):
        jay = Player('Jay')
        self.assertEqual(jay.name, 'Jay')
        self.assertEqual(jay.hand, [])

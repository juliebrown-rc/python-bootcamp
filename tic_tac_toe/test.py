import main
import unittest

class Test_TestTicTacToe(unittest.TestCase):
    def test_move_to_coordinates_x(self):
        # [7,8,9]
        # [4,5,6]
        # [1,2,3]

        # 1 --> (0,0)
        # 2 --> (0,1)
        # 3 --> (0,2)
        # 4 --> (1,0)
        # 5 --> (1,1)
        # 6 --> (1,2)
        # 7 --> (2,0)
        # 8 --> (2,1)
        # 9 --> (2,2)

        moves = list(range(1,10))
        coordinates = [(2, 0), (2, 1), (2, 2),
                       (1, 0), (1, 1), (1, 2),
                       (0, 0), (0, 1), (0, 2)]
        for index, move in enumerate(moves):
            self.assertEqual(main.move_to_coordinates(move)[0], coordinates[index][0])

    def test_move_to_coordinates_y(self):
        moves = list(range(1,10))
        coordinates = [(2, 0), (2, 1), (2, 2),
                       (1, 0), (1, 1), (1, 2),
                       (0, 0), (0, 1), (0, 2)]
        # check x coordinates
        for index, move in enumerate(moves):
            self.assertEqual(main.move_to_coordinates(move)[1], coordinates[index][1])

    def test_check_for_win_row(self):
        board = [[7,8,9],
                 [4,5,6],
                 [1,2,3]]
        
        self.assertEqual(main.check_for_win(board), False)
        board = [[7,8,9],
                 ['X','X','X'],
                 [1,2,3]]
        
        self.assertEqual(main.check_for_win(board), True)

    def test_check_for_win_column(self):
        board = [[7,'O',9],
                 [4,'O',6],
                 [1,'O',3]]

        self.assertEqual(main.check_for_win(board), True)

    def test_for_win_diag(self):
        board = [['X', 8, 9],
                 [4, 'X', 6],
                 [1, 2, 'X']]
        self.assertEqual(main.check_for_win(board), True)

        board = [[7, 8, 'O'],
                 [4, 'O', 6],
                 ['O', 2, 3]]
        self.assertEqual(main.check_for_win(board), True)

    def test_is_legal_move(self):
        board = [['O', 8, 9],
                 [4, 'X', 6],
                 [1, 2, 'X']]
        
        self.assertEqual(main.is_legal_move(board, 7), False)
        self.assertEqual(main.is_legal_move(board, 3), False)
        self.assertEqual(main.is_legal_move(board, 4), True)
        self.assertEqual(main.is_legal_move(board, 2), True)

if __name__ == '__main__':
    unittest.main()

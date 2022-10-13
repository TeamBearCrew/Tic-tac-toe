import TicTacToe
import unittest

class testTicTac(unittest.TestCase):

    def board_create(self):
        board = list(range(1, 10))
        test_case = "-------------\n\
        | 1 | 2 | 3 |\n\
         -------------\n\
        | 4 | 5 | 6 |\n\
         -------------\n\
        | 7 | 8 | 9 |\n\
         -------------"
        test_value = TicTacToe.dashboard(board)
        self.assertEqual(test_case, test_value)

    if __name__ == "__main__":
        unittest.main()
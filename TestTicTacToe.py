import unittest
import TicTacToe

class testTicTacToe(unittest.TestCase):
    board = list(range(1, 10))

    def test_one(self):
        test_case = "-------------\n| 1 | 2 | 3 |\n-------------\n| 4 | 5 | 6 |\n-------------\n| 7 | 8 | 9 |\n-------------"
        self.assertEqual(test_case, TicTacToe.dashboard(board=list(range(1,10))))

    def test_two(self):
        test_case = "-------------\n| 1 | 2 | 3 |\n-------------\n| 4 | 5 | 6 |\n-------------\n| 7 | 8 | 9 |\n-------------"
        self.assertEqual(test_case, TicTacToe.dashboard(board=list(range(5, 8))))


if __name__ == "__main__":
    unittest.main()
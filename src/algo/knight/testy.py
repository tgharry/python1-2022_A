import unittest

from game import get_min_moves

class TaskATests(unittest.TestCase):

    def test_1(self):
        self.assertLess(get_min_moves(target_x=2, target_y=4, start_x=10, start_y=10, chess_board_size=12), -1)

    def test_2(self):
        self.assertLess(get_min_moves(1,2,3,4,5), -1)

    def test_3(self):
        self.assertLess(get_min_moves(2,3,4,5,6), -1)

    def test_4(self):
        self.assertLess(get_min_moves(1,1,4,4,10), -1)

    def test_5(self):
        self.assertLess(get_min_moves(12,12,24,24,48), -1)

    def test_6(self):
        self.assertLess(get_min_moves(1,1,1,1,2), -1)


if __name__ == '__main__':
    unittest.main()

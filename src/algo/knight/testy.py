import unittest

from game import get_min_moves

class TaskATests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(get_min_moves(target_x=2, target_y=4, start_x=10, start_y=10, chess_board_size=12))

    def test_2(self):
        self.assertTrue(get_min_moves(1,2,3,4,5))

    def test_3(self):
        self.assertTrue(get_min_moves(2,3,4,5,6))

    def test_4(self):
        self.assertTrue(get_min_moves(1,1,4,4,10))

    def test_5(self):
        self.assertTrue(get_min_moves(12,12,24,24,48))

    def test_6(self):
        self.assertTrue(get_min_moves(1,1,1,1,2))


if __name__ == '__main__':
    unittest.main()

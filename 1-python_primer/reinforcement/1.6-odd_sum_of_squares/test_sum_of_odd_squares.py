import unittest
from odd_square_sum import sum_of_odd_squares

class TestSumOfOddSquares(unittest.TestCase):
    def test_sum_of_odd_squares(self):
        self.assertEqual(sum_of_odd_squares(1), 0)
        self.assertEqual(sum_of_odd_squares(2), 1)
        self.assertEqual(sum_of_odd_squares(5), 10)
        self.assertEqual(sum_of_odd_squares(7), 35)

if __name__ == '__main__':
    unittest.main()

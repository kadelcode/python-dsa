import unittest
from sum_of_squares import sum_of_squares

class TestSumOfSquares(unittest.TestCase):
    """
    This class defines unit tests for the sum_of_squares function.
    """

    def test_base_cases(self):
        """
        Tests the function for base cases (n <= 1).
        """
        self.assertEqual(sum_of_squares(0), 0)
        self.assertEqual(sum_of_squares(1), 1)

    def test_larger_values(self):
        """
        Tests the function for larger values of n.
        """
        self.assertEqual(sum_of_squares(10), 285)
        self.assertEqual(sum_of_squares(20), 2470)

if __name__ == '__main__':
    unittest.main()

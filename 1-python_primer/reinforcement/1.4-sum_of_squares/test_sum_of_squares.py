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

if __name__ == '__main__':
    unittest.main()

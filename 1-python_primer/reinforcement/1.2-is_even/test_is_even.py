import unittest
from is_even import is_even

class TestIsEven(unittest.TestCase):
    """
    Unit tests for the is_even function.
    """

    def test_even_number(self):
        """
        Tests if the function correctly identifies an even number.
        """
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        """
        Tests if the function correctly identifies an odd number
        """
        self.assertFalse(is_even(11))

    def test_zero(self):
        """
        Test if the function correctly identifies zero as even.
        """
        self.assertTrue(is_even(0))

if __name__ == "__main__":
    unittest.main()

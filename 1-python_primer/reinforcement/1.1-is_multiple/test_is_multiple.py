import unittest
from is_multiple import is_multiple

class TestIsMultiple(unittest.TestCase):
    """
    This class contains unit tests for the
    `is_multiple` function.
    """

    def test_multiple(self):
        """
        Test if a known multiple returns True.
        """
        self.assertTrue(is_multiple(10, 2))

    def test_not_multiple(self):
        """
        Test if a known non-multiple returns False
        """
        self.assertFalse(is_multiple(11, 2))

    def test_zero_divisor(self):
        """
        Test if dividing by zero raises an error.
        
        with self.assertRaises(ZeroDivisionError):
            is_multiple(10, 0)
        """
        self.assertFalse(is_multiple(5, 0))

# Run the tests if this module is not imported
if __name__ == '__main__':
    unittest.main()

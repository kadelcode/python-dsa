import unittest
from minmax import minmax

class TestMinmax(unittest.TestCase):
    """
    Unit tests for the minmax function
    """

    def test_empty_list(self):
        """
        Tests if the function raises an error for an empty list.
        """
        with self.assertRaises(ValueError):
            minmax([])

    def test_data_not_a_list(self):
        """
        Tests if the function raises an error if data is not list
        """
        with self.assertRaises(TypeError):
            minmax("123")

    def test_single_element(self):
        """
        Tests if the function returs the same value for a single element
        """
        self.assertEqual(minmax([5]), (5,5))

if __name__ == '__main__':
    unittest.main()

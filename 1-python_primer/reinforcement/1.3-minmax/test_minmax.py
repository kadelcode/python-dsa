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

    def test_sorted_list(self):
        """
        Tests if the function correctly finds min and
        max for a sorted list
        """
        self.assertEqual(minmax([1, 2, 3, 4, 5]), (1, 5))

    def test_unsorted_list(self):
        """
        Tests if the function correctly finds the min and
        max for an unsorted list
        """
        self.assertEqual(minmax([6, 5, 20, 3, 7]), (3, 20))

if __name__ == '__main__':
    unittest.main()

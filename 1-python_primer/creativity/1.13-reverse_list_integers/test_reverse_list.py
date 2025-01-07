import unittest
from reverse_list import reverse_list

class TestReverseList(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_empty(self):
        self.assertEqual(reverse_list([]), [])

    def test_single_element(self):
        self.assertEqual(reverse_list([20]), [20])

    def test_negative_numbers(self):
        self.assertEqual(reverse_list([-1, -2, -3, -4]), [-4, -3, -2, -1])

    def test_duplicates(self):
        self.assertEqual(reverse_list([1, 1, 2, 2, 3, 3]), [3, 3, 2, 2, 1, 1])


if __name__ == "__main__":
    unittest.main()
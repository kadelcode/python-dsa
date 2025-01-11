import unittest
from are_numbers_distinct import are_numbers_distinct

class TestDistinctNumbers(unittest.TestCase):

    def test_unique_numbers(self):
        self.assertEqual(are_numbers_distinct([1, 2, 3, 4, 5]), True)

    def test_no_unique_numbers(self):
        self.assertEqual(are_numbers_distinct([1, 2, 2, 3, 4]), False)

    def test_empty_sequence(self):
        self.assertEqual(are_numbers_distinct([]), True)


if __name__ == "__main__":
    unittest.main()
import unittest
from count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfgh"), 0)

    def test_all_vowels_lowercase(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_all_vowels_uppercase(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_with_numbers_and_symbols(self):
        self.assertEqual(count_vowels("123!@#aBcDe"), 2)

if __name__ == "__main__":
    unittest.main()
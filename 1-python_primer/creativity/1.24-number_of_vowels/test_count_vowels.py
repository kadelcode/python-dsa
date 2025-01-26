import unittest
from count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfgh"), 0)

    def test_all_vowels_lowercase(self):
        self.assertEqual(count_vowels("aeiou"), 5)

if __name__ == "__main__":
    unittest.main()
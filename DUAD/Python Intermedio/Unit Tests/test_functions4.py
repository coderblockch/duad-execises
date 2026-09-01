import unittest
from functions4 import reverse_string


class TestReverseString(unittest.TestCase):
    
    def test_phrase(self):
        self.assertEqual(reverse_string("Hola mundo"), "odnum aloH")
    
    def test_single_word(self):
        self.assertEqual(reverse_string("python"), "nohtyp")
    
    def test_short_string(self):
        self.assertEqual(reverse_string("abc"), "cba")


if __name__ == '__main__':
    unittest.main()
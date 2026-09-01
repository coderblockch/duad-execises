import unittest
from functions5 import count_cases


class TestCountCases(unittest.TestCase):
    
    def test_mixed_phrase(self):
        self.assertEqual(count_cases("I love Nación Sushi"),
                         "There's 3 upper cases and 13 lower cases")
    
    def test_all_upper(self):
        self.assertEqual(count_cases("ABC"),
                         "There's 3 upper cases and 0 lower cases")
    
    def test_all_lower(self):
        self.assertEqual(count_cases("hello"),
                         "There's 0 upper cases and 5 lower cases")


if __name__ == '__main__':
    unittest.main()
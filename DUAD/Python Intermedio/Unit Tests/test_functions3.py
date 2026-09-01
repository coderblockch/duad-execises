import unittest
from functions3 import sum_list


class TestSumList(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(sum_list([4, 6, 2, 29]), 41)
    
    def test_with_zero(self):
        self.assertEqual(sum_list([0, 10, 5]), 15)
    
    def test_negative_numbers(self):
        self.assertEqual(sum_list([-5, 5, 10]), 10)


if __name__ == '__main__':
    unittest.main()
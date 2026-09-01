import unittest
from functions7 import get_primes


class TestGetPrimes(unittest.TestCase):
    
    def test_mixed_numbers(self):
        self.assertEqual(get_primes([1, 4, 6, 7, 13, 9, 67]), [7, 13, 67])
    
    def test_small_primes(self):
        self.assertEqual(get_primes([2, 3, 4, 5]), [2, 3, 5])
    
    def test_no_primes(self):
        self.assertEqual(get_primes([1, 4, 6, 8, 9]), [])


if __name__ == '__main__':
    unittest.main()
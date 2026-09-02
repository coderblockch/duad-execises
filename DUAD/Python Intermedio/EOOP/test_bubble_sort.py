import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    
    def test_small_list(self):
        result = bubble_sort([5, 2, 8, 1])
        self.assertEqual(result, [1, 2, 5, 8])

    def test_large_list(self):
        big_list = list(range(100, 0, -1))
        result = bubble_sort(big_list)
        expected = list(range(1, 101))
        self.assertEqual(result, expected)

    def test_empty_list(self):
        result = bubble_sort([])
        self.assertEqual(result, [])

    def test_not_a_list(self):
        with self.assertRaises(TypeError):
            bubble_sort(123)


if __name__ == '__main__':
    unittest.main()
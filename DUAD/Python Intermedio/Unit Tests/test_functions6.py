import unittest
from functions6 import sort_words


class TestSortWords(unittest.TestCase):
    
    def test_five_words(self):
        self.assertEqual(
            sort_words("python-variable-funcion-computadora-monitor"),
            "computadora-funcion-monitor-python-variable"
        )
    
    def test_three_words(self):
        self.assertEqual(
            sort_words("banana-apple-cherry"),
            "apple-banana-cherry"
        )
    
    def test_two_words(self):
        self.assertEqual(
            sort_words("zebra-ant"),
            "ant-zebra"
        )


if __name__ == '__main__':
    unittest.main()
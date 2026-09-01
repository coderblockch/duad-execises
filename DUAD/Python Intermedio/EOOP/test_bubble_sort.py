import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    
    def test_small_list(self):
        result = bubble_sort([5, 2, 8, 1])
        self.assertEqual(result, [1, 2, 5, 8])

    def test_large_list(self):
        # Creamos una lista de 100 a 1 (desordenada, al revés)
        big_list = list(range(100, 0, -1))    # [100, 99, ..., 1]
        result = bubble_sort(big_list)
        # Lo esperado: ordenada de 1 a 100
        expected = list(range(1, 101))         # [1, 2, ..., 100]
        self.assertEqual(result, expected) 

    def test_empty_list(self):
        result = bubble_sort([])
        self.assertEqual(result, [])      


    def bubble_sort(arr):
        if not isinstance(arr, list):
         raise TypeError("The parameter must be a list")
        n = len(arr)
        for i in range(n):
         for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr  


    def test_not_a_list(self):
        with self.assertRaises(TypeError):
            bubble_sort(123)    # 123 no es lista → debe lanzar TypeError   





if __name__ == '__main__':
    unittest.main()
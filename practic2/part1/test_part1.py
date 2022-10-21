import unittest
from count_sort import counting_sort

class TestCountSort(unittest.TestCase):

    def test_EmptyArr(self):
        data =[]
        self.assertEqual(counting_sort(data), [])

    def test_SingleNum(self):
        data = [1]
        self.assertEqual(counting_sort(data), [1])

    def test_ManySingleNum(self):
        data = [1, 1, 1, 1, 1, 1]
        self.assertEqual(counting_sort(data), [1, 1, 1, 1, 1, 1])

    def test_SortArr(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(counting_sort(data), [1, 2, 3, 4, 5])

    def test_UnsortedArr(self):
        data = [3, 0, -1, 9, 2]
        self.assertEqual(counting_sort(data), [-1, 0, 2, 3, 9])

    def test_SortedDublicates(self):
        data = [0, 1, 1, 2, 2, 2, 9]
        self.assertEqual(counting_sort(data), [0, 1, 1, 2, 2, 2, 9])

    def test_UnsortedDublicates(self):
        data = [9, -1, 2, 1, -1, 3, 9, 2]
        self.assertEqual(counting_sort(data), [-1, -1, 1, 2, 2, 3, 9, 9])

    def test_BigNumbers(self):
        data = [1, 0, 1000000, 0, -1000000]
        self.assertEqual(counting_sort(data), [-1000000, 0, 0, 1, 1000000])

if __name__ == '__main__':
    unittest.main()

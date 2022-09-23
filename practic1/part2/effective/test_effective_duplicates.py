import unittest
from effective_duplicates import has_duplicates, get_duplicates


class TestHasDuplacates(unittest.TestCase):

    def test_empty_array(self):
        data = []
        self.assertEqual(has_duplicates(data), False)
        self.assertEqual(get_duplicates(data), [])

    def test_single_element(self):
        data = [1]
        self.assertEqual(has_duplicates(data), False)
        self.assertEqual(get_duplicates(data), [])

    def test_many_elements(self):
        data = [2, 1, -4, 7]
        self.assertEqual(has_duplicates(data), False)
        self.assertEqual(get_duplicates(data), [])

    def test_one_duplicate(self):
        data = [2, -3, 0, 2, 7, 1]
        self.assertEqual(has_duplicates(data), True)
        self.assertEqual(get_duplicates(data), [2])

    def test_many_duplicates(self):
        data = [2, -3, 0, 2, 1, -3, 4, 1, -1, 2]
        self.assertEqual(has_duplicates(data), True)
        self.assertTrue(sorted(get_duplicates(data)) == [-3, 1, 2])

    def test_single_duplicated_elem(self):
        data = [4, 4, 4, 4]
        self.assertEqual(has_duplicates(data), True)
        self.assertEqual(get_duplicates(data), [4])


if __name__ == '__main__':
    unittest.main()

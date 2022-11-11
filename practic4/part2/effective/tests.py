from unittest import TestCase, main
from func import get_max_activities


class TestCountSort(TestCase):
    def test_empty(self):
        self.assertEqual(get_max_activities([]), [])

    def test_one_activity(self):
        self.assertEqual(get_max_activities([[2, 3]]), [[2, 3]])

    def test_two_compatibles(self):
        self.assertEqual(get_max_activities(
            [[3, 4], [2, 3]]), [[2, 3], [3, 4]])

    def test_two_overlaps(self):
        result = get_max_activities([[2, 5], [3, 4]])
        self.assertTrue(result == [[2, 5]] or result == [[3, 4]])

    def test_two_incompatibles(self):
        result = get_max_activities([[3, 6], [2, 5]])
        self.assertTrue(result == [[2, 5]] or result == [[3, 6]])

    def test_three_activities(self):
        self.assertEqual(get_max_activities(
            [[2, 6], [1, 4], [5, 8]]), [[1, 4], [5, 8]])

    def test_four_activities(self):
        result = get_max_activities([[2, 6], [1, 4], [7, 10], [5, 8]])
        self.assertTrue(result == [[1, 4], [5, 8]]
                        or result == [[2, 6], [7, 10]])

    def test_five_activities(self):
        self.assertEqual(get_max_activities(
            [[2, 6], [1, 4], [7, 10], [5, 8], [9, 12]]), [[1, 4], [5, 8], [9, 12]])

    def test_big_one(self):
        result = get_max_activities([[3, 5], [1, 4], [5, 7], [0, 6], [3, 9], [5, 9], [
                                    6, 11], [4, 10], [8, 12], [2, 14], [12, 16]])
        self.assertTrue(result == [[1, 4], [5, 7], [8, 12], [12, 16]] or result == [
                        [3, 5], [5, 7], [8, 12], [12, 16]])


if __name__ == '__main__':
    main()

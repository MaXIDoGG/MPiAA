from unittest import TestCase, main
from Nativ_Func import closest_pair

class TestCountSort(TestCase):
    def test_NoPoints(self):
        with self.assertRaises(Exception) as err:
            closest_pair([])
        self.assertEqual('Точек нет или она одна.', err.exception.args[0])

    def test_SinglePoint(self):
        with self.assertRaises(Exception) as e:
            closest_pair([{'x': 1, 'y': 1}])
        self.assertEqual('Точек нет или она одна.', e.exception.args[0])

    def test_TwoPoints(self):
        self.assertEqual(closest_pair([{'x': 2, 'y': 3}, {'x': 3, 'y': 4}]), ([{'x': 2, 'y': 3}, {'x': 3, 'y': 4}]))

    def test_ThreePoints(self):
        self.assertEqual(closest_pair([{'x': 2, 'y': 3}, {'x': 1, 'y': 9}, {'x': 6, 'y': 2}]), [{'x': 2, 'y': 3},{'x': 6, 'y': 2}])

    def test_DuplicatePoints(self):
        self.assertEqual(closest_pair([{'x': 2, 'y': 3}, {'x': 2, 'y': 3}, {'x': 3, 'y': 4}]), [{'x': 2, 'y': 3},{'x': 2, 'y': 3}])

    def test_SameXcoordinate(self):
        self.assertEqual(closest_pair([{'x': 2, 'y': 9}, {'x': 2, 'y': 1}, {'x': 2, 'y': 4}, {'x': 2, 'y': -8}]), [{'x': 2, 'y': 1},{'x': 2, 'y': 4}])

    def test_ManyPoints(self):
        self.assertEqual(closest_pair([{'x': 2, 'y': 3}, {'x': 0, 'y': 4}, {'x': 11, 'y': 9},
        {'x': 2, 'y': 8}, {'x': 4, 'y': 4}, {'x': 3, 'y': 6}, {'x': 6, 'y': 5}, {'x': 1, 'y': 9}]), [{'x': 1, 'y': 9},{'x': 2, 'y': 8}])

    def test_NegativePoits(self):
        self.assertEqual(closest_pair([{'x': -5, 'y': 6}, {'x': 1, 'y': 2}, {'x': 4, 'y': -2}, {'x': -9, 'y': 0},
        {'x': -1, 'y': -2}, {'x': 0, 'y': 7}, {'x': 2, 'y': -1}, {'x': -3, 'y': 1}]), [{'x': 2, 'y': -1},{'x': 4, 'y': -2}])

    def test_ClosestPointsAreFromStripe(self):
        self.assertEqual(closest_pair([{'x': -1, 'y': 20}, {'x': -1.5, 'y': 10}, {'x': -2, 'y': -10},{'x': -2.7, 'y': -20},
         {'x': -10, 'y': 20}, {'x': -10.5, 'y': 10}, {'x': -11.7, 'y': -10}, {'x': -12.2, 'y': -20},
         {'x': 1, 'y': 21}, {'x': 1.5, 'y': 11}, {'x': 2, 'y': -9},{'x': 2.7, 'y': -19},
         {'x': 10, 'y': 21}, {'x': 10.5, 'y': 11}, {'x': 11.7, 'y': -9},{'x': 12.2, 'y': -19},]), [{'x': -1, 'y': 20},{'x': 1, 'y': 21}])

if __name__ == '__main__':
    main()

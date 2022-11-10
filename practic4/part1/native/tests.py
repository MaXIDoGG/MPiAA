from unittest import TestCase, main
from func import nativeLcs


class TestCountSort(TestCase):
    def test_empty_two(self):
        self.assertEqual(nativeLcs('', ''), '')

    def test_empty_one(self):
        self.assertEqual(nativeLcs('', 'abcd'), '')
        self.assertEqual(nativeLcs('', ''), '')

    def test_equal(self):
        self.assertEqual(nativeLcs('abcd', 'abcd'), 'abcd')

    def test_substring(self):
        self.assertEqual(nativeLcs('abab', 'ab'), 'ab')

    def test_substring_middle(self):
        self.assertEqual(nativeLcs('xyaban', 'abarab'), 'aba')

    def test_substring_subsequences(self):
        self.assertEqual(nativeLcs('nahybser', 'iunkayxbis'), 'naybs')
        self.assertEqual(nativeLcs('z1artunx', 'yz21rx'), 'z1rx')
        self.assertEqual(nativeLcs('z1arxzyx1a', 'yz21rx'), 'z1rx')
        self.assertEqual(nativeLcs('yillnum', 'numyjiljil'), 'yill')

    def test_reverse(self):
        result = nativeLcs('xablar', 'ralbax')
        self.assertTrue(result == 'aba' or result == 'ala')


if __name__ == '__main__':
    main()

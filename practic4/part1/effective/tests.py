from unittest import TestCase, main
from func import LCS_DYN


class TestCountSort(TestCase):
    def test_empty_two(self):
        self.assertEqual(LCS_DYN('', ''), '')

    def test_empty_one(self):
        self.assertEqual(LCS_DYN('', 'abcd'), '')
        self.assertEqual(LCS_DYN('', ''), '')

    def test_equal(self):
        self.assertEqual(LCS_DYN('abcd', 'abcd'), 'abcd')

    def test_substring(self):
        self.assertEqual(LCS_DYN('abab', 'ab'), 'ab')

    def test_substring_middle(self):
        self.assertEqual(LCS_DYN('xyaban', 'abarab'), 'aba')

    def test_substring_subsequences(self):
        self.assertEqual(LCS_DYN('nahybser', 'iunkayxbis'), 'naybs')
        self.assertEqual(LCS_DYN('z1artunx', 'yz21rx'), 'z1rx')
        self.assertEqual(LCS_DYN('z1arxzyx1a', 'yz21rx'), 'z1rx')
        self.assertEqual(LCS_DYN('yillnum', 'numyjiljil'), 'yill')

    def test_reverse(self):
        result = LCS_DYN('xablar', 'ralbax')
        self.assertTrue(result == 'aba' or result == 'ala')


if __name__ == '__main__':
    main()

import unittest
from main import Dictionary


class TestDictionary(unittest.TestCase):

    def test_empty_dict(self):
        d = Dictionary(10)
        self.assertEqual(d.size(), 0)
        self.assertEqual(d.get('hello'), '')

    def test_one_item(self):
        d = Dictionary(10)
        d.set('friend', 'amigo')
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.get('friend'), 'amigo')

    def test_several_items(self):
        d = Dictionary(10)
        d.set("friend", "amigo")
        d.set("dog", "perro")
        d.set("cat", "gato")
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.get('friend'), 'amigo')
        self.assertEqual(d.get('dog'), 'perro')
        self.assertEqual(d.get('cat'), 'gato')

    def test_duplicate_keys(self):
        d = Dictionary(10)
        d.set("beer", "beer")
        d.set("cat", "gato")
        d.set("beer", "cerveza")
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.get('beer'), 'cerveza')

    def test_duplicate_values(self):
        d = Dictionary(10)
        d.set("hello", "hola")
        d.set("friend", "amigo")
        d.set("hi", "hola")
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.get('hello'), 'hola')
        self.assertEqual(d.get('hi'), 'hola')

    def test_case_sensitive(self):
        d = Dictionary(10)
        d.set("big", "grande")
        d.set("BIG", "GRANDE")
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.get('big'), 'grande')
        self.assertEqual(d.get('BIG'), 'GRANDE')

    def test_anagrams(self):
        d = Dictionary(10)
        d.set("abc", "uno")
        d.set("bac", "dos")
        d.set("cba", "tres")
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.get('abc'), 'uno')
        self.assertEqual(d.get('bac'), 'dos')
        self.assertEqual(d.get('cba'), 'tres')

    def test_same_first_letter(self):
        d = Dictionary(10)
        d.set("hello", "hola")
        d.set("house", "casa")
        d.set("human", "humano")
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.get('hello'), 'hola')
        self.assertEqual(d.get('house'), 'casa')
        self.assertEqual(d.get('human'), 'humano')

    def test_user_hash_func(self):
        def hashF2(size, key):  # метод умножения
            sum = 0
            for i in key:
                sum += ord(i)
            return round(size * ((0.618 * sum) % 1))-1
        d = Dictionary(10, hashF2)
        d.set("s1", "Short string")
        d.set("s2", "Another short string")
        d.set("long", "Long string")
        d.set("long", "Longer string")
        d.set("long long long", "Very very long string")
        self.assertEqual(d.size(), 4)
        self.assertEqual(d.get('s2'), 'Another short string')
        self.assertEqual(d.get('long long long'), 'Very very long string')


if __name__ == '__main__':
    unittest.main()

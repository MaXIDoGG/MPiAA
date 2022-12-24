from unittest import TestCase, main
from fu import Prim

class TestsPrim(TestCase):
    def  testEmpty(self):
        g = []
        self.assertEqual(Prim(g, 0), {})

    def testSingleVertex(self):
        g = [[0]]
        self.assertEqual(Prim(g, 0), {})

    def testOneEdge(self):
        g = [[0, 2.5],
            [2.5, 0]]
        self.assertEqual(Prim(g, 0), {(2.5, 0, 1)})

    def testTwoEdges(self):
        g = [[0, 2.5, 0],
            [2.5, 0, 1.0],
            [0, 1.0, 0]]
        self.assertEqual(Prim(g, 0), {(2.5, 0, 1), (1.0, 1, 2)})

    def testThreeEdges(self):
        g = [[0, 2.5, 0.7],
             [2.5, 0, 1.0],
             [0.7, 1.0, 0]]
        self.assertEqual(Prim(g, 0), {(0.7, 0, 2), (1.0, 2, 1)})

    def testManyEdges(self):
        g = [[0, 4, 0, 0, 0, 0, 0, 9, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 1, 6],
             [9, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]]
        self.assertEqual(Prim(g, 0), {(4, 0, 1), (8, 1, 2), (7, 2, 3), (9, 3, 4), (4, 2, 5), (2, 2, 8), (2, 5, 6), (1, 6, 7)})


if __name__ == '__main__':
    main()
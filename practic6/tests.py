from unittest import TestCase, main
# from BruteForce import TSP
from greedy import TSP


class TestsTSP(TestCase):
    def testEmpty(self):
        g = []
        self.assertEqual(TSP(g, 0), [])

    def testSingleVertex(self):
        g = [[0]]
        self.assertEqual(TSP(g, 0), [])

    def testOneEdge(self):
        g = [[0, 2.5],
             [2.5, 0]]
        self.assertEqual(TSP(g, 0), [0, 1])

    def testThreeEdges(self):
        g = [[0, 2.5, 0.5],
             [2.5, 0, 1],
             [0.5, 1, 0]]
        self.assertEqual(TSP(g, 0), [0, 2, 1])

    def testSeveralVertices(self):
        g = [[0, 6, 4, 1],
             [6, 0, 3.5, 2],
             [4, 3.5, 0, 5],
             [1, 2, 5, 0]]
        self.assertEqual(TSP(g, 0), [0, 3, 1, 2])

    def testManyVertices(self):
        g = [[0, 2, 4, 1, 2.5],
             [2, 0, 3.6, 6, 3],
             [4, 3.6, 0, 7, 5],
             [1, 6, 7, 0, 9],
             [2.5, 3, 5, 9, 0]]
        self.assertEqual(TSP(g, 0), [0, 3, 2, 1, 4])

    def testUnreachableVertex(self):
        g = [[0, 2.5, 1, 0, 0],
             [2.5, 0, 1, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0.7],
             [0, 0, 0, 0.7, 0]]
        self.assertEqual(TSP(g, 0), [])
        self.assertEqual(TSP(g, 3), [])

    def testNoLoopedPath(self):
        g = [[0, 2.5, 1, 0],
             [2.5, 0, 0, 0],
             [1, 0, 0, 7],
             [0, 0, 7, 0]]
        self.assertEqual(TSP(g, 0), [])
        self.assertEqual(TSP(g, 1), [])


if __name__ == '__main__':
    main()

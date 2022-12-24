from unittest import TestCase, main
from fu import Dijkstra

class TestsDijkstra(TestCase):
    def testEmpty(self):
        G = []
        self.assertEqual(Dijkstra(G, 0, 1), [])

    def testOneVertex(self):
        G = [[0, 2.5, 3.0],
            [2.5, 0 , 0],
            [3.0, 0, 0]]
        self.assertEqual(Dijkstra(G, 0, 1), [0, 1])

    def testOneEdges(self):
        G = [[0, 2.5],
            [2.5, 0]]
        self.assertEqual(Dijkstra(G, 0, 1), [0, 1])

    def testTwoEdges(self):
        G = [[0, 2.5, 1.0],
            [2.5, 0 , 0],
            [1.0, 0, 0]]
        self.assertEqual(Dijkstra(G, 0, 1), [0, 1])
    
    def testThreeEdges(self):
        G = [[0, 2.5, 1.0],
            [2.5, 0 , 0.7],
            [1.0, 0.7, 0]]
        self.assertEqual(Dijkstra(G, 0, 1), [0, 2, 1])
    
    def testManyEdges(self):
        G = [[0, 3.0, 2.0, 0, 5.0],
            [2.5, 0 , 0.5, 2.0, 0],
            [2.0, 0.5, 0, 0.5, 2.0],
            [0, 2.0, 0.5, 0, 1.0],
            [5.0, 0, 2.0, 1.0, 0]]
        self.assertEqual(Dijkstra(G, 0, 4), [0, 2, 3, 4])
        self.assertEqual(Dijkstra(G, 4, 0), [4, 3, 2, 0])
        self.assertEqual(Dijkstra(G, 1, 4), [1, 2, 3, 4])

    def testUnreachableVertex(self):
        G = [[0, 2.5, 1.0, 0, 0],
            [2.5, 0 , 1.0, 0, 0],
            [1.0, 1.0, 0, 0, 0],
            [0, 0, 0, 0, 0.7],
            [0, 0, 0, 0.7, 0]]
        self.assertEqual(Dijkstra(G, 0, 4), 'пути нет')
        self.assertEqual(Dijkstra(G, 3, 0), 'пути нет')

if __name__ == '__main__':
    main()
from Ejercicio10 import n_edges
import unittest

class TestEdges(unittest.TestCase):
    
    def testEdges_1(self):
        self.assertEqual(
            n_edges([[0, 1], [1, 2], [2, 3], [3, 4]], 5), 1), "Should be 1"

    def testEdges_2(self):
        self.assertEqual(
            n_edges([[0, 1], [2, 3], [4, 5], [6, 6]], 7), 4), "Should be 4"

    def testEdges_3(self):
        self.assertEqual(
            n_edges([[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]], 11), 2), "Should be 2"

    def testEdges_4(self):
        self.assertEqual(
            n_edges([[0, 1], [1, 2], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]], 11), 3), "Should be 3"

    def testEdges_5(self):
        self.assertEqual(
            n_edges([[0, 1], [1, 2], [3, 4]], 5), 2), "Should be 2"

unittest.main()
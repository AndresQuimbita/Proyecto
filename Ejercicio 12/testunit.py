from Ejercicio12 import path
import unittest
import math


class TestTree(unittest.TestCase):

    def testTree_1(self):
        A = [3, 9, 8, 4, 0, 1, 7]
        self.assertEqual(path(A, int(math.log2(len(A)+1))),
                         [[4], [9], [3, 0, 1], [8], [7]]), "Should be [[4], [9], [3, 0, 1], [8], [7]]"

    def testTree_2(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
             17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        self.assertEqual(path(A, int(math.log2(len(A)+1))),
                         [[16], [8], [4, 17, 18, 19, 20], [2, 9, 10, 11], [1, 21, 22, 23, 24, 25, 26, 5, 6], [3, 12, 13, 14], [7, 27, 28, 29, 30], [15], [31]]), "Should be [-23, -5, 1, 7]"

    def testTree_3(self):
        A = [3, 9, 20]
        self.assertEqual(path(A, int(math.log2(len(A)+1))),
                         [[9], [3], [20]]), "Should be [[9], [3], [20]]"

    def testTree_4(self):
        A = []
        self.assertEqual(path(A, int(math.log2(len(A)+1))), []), "Should be []"

    def testTree_5(self):
        A = [3, 9, 8, 4, 0, 1, 7, None, None, 5, None, None, 2, None, None]
        self.assertEqual(path(A, int(math.log2(len(A)+1))), [[4], [9, 5], [3, 0, 1], [
                         8, 2], [7]]), "Should be [[4], [9, 5], [3, 0, 1], [8, 2], [7]]"


unittest.main()

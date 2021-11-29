from Ejercicio9 import insert_Value
import unittest


class TestList(unittest.TestCase):

    def testList_1(self):
        self.assertEqual(insert_Value([3, 4, 5, 7, 1, 2], 6), [
                         3, 4, 5, 6, 7, 1, 2]), "Should be [3, 4, 5, 6, 7, 1, 2]"

    def testList_2(self):
        self.assertEqual(insert_Value([], -1), [-1]), "Should be [-1]"

    def testList_3(self):
        self.assertEqual(insert_Value([3, 4, 1], 2), [
                         3, 4, 1, 2]), "Should be [3, 4, 1, 2]"

    def testList_4(self):
        self.assertEqual(insert_Value(
            [-1, 1, 5, 6], -2), [-1, 1, 5, 6, -2]), "Should be [-1, 1, 5, 6, -2]"

    def testList_5(self):
        self.assertEqual(insert_Value([3, 4, 1, 2], 5), [
                         3, 4, 5, 1, 2]), "Should be [3, 4, 5, 1, 2]"


unittest.main()

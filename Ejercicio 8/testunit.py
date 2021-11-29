from Ejercicio8 import queries_array
import unittest


class TestQueries(unittest.TestCase):

    def testQueries_1(self):
        self.assertEqual(queries_array([[1, 4], [2, 4], [3, 6], [4, 4]], [
                         2, 3, 4, 5]), [3, 3, 1, 4]), "Should be [3, 3, 1, 4]"

    def testQueries_2(self):
        self.assertEqual(queries_array([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]), [
                         2, -1, 4, 6]), "Should be [2, -1, 4, 6]"

    def testQueries_3(self):
        self.assertEqual(queries_array([[2, 8], [2, 4], [3, 8], [21, 24]], [
                         7, 6, 1, 25]), [6, 6, -1, -1]), "Should be [6, 6, -1, -1]"

    def testQueries_4(self):
        self.assertEqual(queries_array(
            [[-8, 3], [-8, 0], [0, 4], [9, 9]], [-3, 2, 1, 9]), [9, 5, 5, 1]), "Should be [9, 5, 5, 1]"

    def testQueries_5(self):
        self.assertEqual(queries_array(
            [[-1, 0], [-2, -2], [3, 8], [4, 8]], [-1, 0, 78, 1]), [2, 2, -1, -1]), "Should be [2, 2, -1, -1]"


unittest.main()

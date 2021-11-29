from Ejercicio1 import cuadratic_function, Array
import unittest


class TestCuadratic(unittest.TestCase):

    def testArray_cuadratic_1(self):
        self.assertEqual(cuadratic_function(Array(
            4, [-4, -2, 2, 4]), 1, 3, 5).arr, [3, 9, 15, 33]), "Should be [3,9,15,33]"

    def testArray_cuadratic_2(self):
        self.assertEqual(cuadratic_function(Array(
            4, [-4, -2, 2, 4]), -1, 3, 5).arr, [-23, -5, 1, 7]), "Should be [-23, -5, 1, 7]"

    def testArray_cuadratic_3(self):
        self.assertEqual(cuadratic_function(Array(6, [-9, -8, 0, 1, 8, 9]), 0, -6, -10).arr, [
                         -64, -58, -16, -10, 38, 44]), "Should be [-64, -58, -16, -10, 38, 44]"

    def testArray_cuadratic_4(self):
        self.assertEqual(cuadratic_function(Array(
            7, [0, 0, 0, 0, 0, 0, 1]), 0, 0, -10).arr, [-10, -10, -10, -10, -10, -10, -10]), "Should be [-10, -10, -10, -10, -10, -10, -10]"

    def testArray_cuadratic_5(self):
        self.assertEqual(cuadratic_function(Array(6, [-1, 0, 3, 4, 9, 12]), -1/2, -6/7, -10).arr, [-92.28571428571428, -
                         58.214285714285715, -21.42857142857143, -17.07142857142857, -10.0, -9.642857142857142]), "Should be [3,9,15,33]"

    def testArray_cuadratic_6(self):
        self.assertEqual(cuadratic_function(
            Array(0, []), -1/2, -6/7, -10), []), "Should be []"

    def testArray_cuadratic_7(self):
        self.assertEqual(cuadratic_function(
            Array(1, [0]), -1/2, -6/7, -10), [-10]), "Should be [-10]"


unittest.main()

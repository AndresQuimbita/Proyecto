from Ejercicio6 import impar_odd_sum
import unittest


class TestOddSum(unittest.TestCase):

    def testOdd_1(self):
        self.assertEqual(impar_odd_sum([1, 3, 5]), 4), "Should be 4"

    def testOdd_2(self):
        self.assertEqual(impar_odd_sum([2, 4, 6]), 0), "Should be 0"

    def testOdd_3(self):
        self.assertEqual(impar_odd_sum([5, 4, 4, 5, 1, 3]), 12), "Should be 12"

    def testOdd_4(self):
        self.assertEqual(impar_odd_sum([5, 4, 4, 5, 1, 3, 9, 8, 7, 12, 12, 16,
                         789, 45, 13, 132, 132, -4, 113, 12313, 132]), 117), "Should be 117"

    def testOdd_5(self):
        self.assertEqual(impar_odd_sum([5, 4, 4, 5, 1, 3, 9, 8, 7, 12, 12, 16,
                         789, 45, 13, 132, 132, -4, 113, 12313, 132, 897, 78944213, 489, 4564, 894, 564, 987465, 123]), 225), "Should be 225"


unittest.main()

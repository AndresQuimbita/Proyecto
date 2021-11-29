from Ejercicio4 import find_observations
import unittest


class TestObservations(unittest.TestCase):

    def testFind_1(self):
        self.assertEqual(find_observations([3, 2, 4, 3], 4, 2), [
                         6, 6]), "Should be [6,6]"

    def testFind_2(self):
        self.assertEqual(find_observations([1, 5, 6], 3, 4), [
                         2, 2, 2, 3]), "Should be [2,2,2,3]"

    def testFind_3(self):
        self.assertEqual(find_observations(
            [1, 2, 3, 4], 6, 4), []), "Should be []"

    def testFind_4(self):
        self.assertEqual(find_observations(
            [1], 3, 1), [5]), "Should be [5]"

    def testFind_5(self):
        self.assertEqual(find_observations(
            [0, 0], 0, 2), [0, 0]), "Should be [0,0]"


unittest.main()

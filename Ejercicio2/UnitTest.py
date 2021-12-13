import Ejercicio_2
import unittest


class TestRandomized(unittest.TestCase):

    def testRandomizedSet_1(self):
        self.assertEqual(input([["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],[[], [1], [2], [2], [], [1], [2], []]]),[None, True, False, True, 2, True, False, 2])


    def testRandomizedSet_2(self):
        self.assertTrue(input([["RandomizedSet","remove", "insert","getRandom"],[[], [1], [1],[]]]),[None, False, True, 1])


if __name__ == '__main__':
    unittest.main()


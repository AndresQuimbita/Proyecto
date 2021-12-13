import Ejercicio_2
import unittest


class TestRandomized(unittest.TestCase):

    def testRandomizedSet_1(self):
        self.assertEqual(input(["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],[[], [1], [2], [2], [], [1], [2], []])),"Should be [null, true, false, true, Rand(1-2), true, false, 2]"


    def testRandomizedSet_2(self):
        self.assertTrue(input(["RandomizedSet","remove", "insert","getRandom"],[[], [1], [1],[]])),"Should be [null, false, true, 1]"


if __name__ == '__main__':
    unittest.main()

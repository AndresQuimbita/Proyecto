from  Ejercicio_7 import count_paths
import unittest


class TestCountPaths(unittest.TestCase):

    def testCount_1(self):
        self.assertEqual(count_paths([2,4,6,8,10]),7),"Should be 7"

    def testCount_2(self):
        self.assertEqual(count_paths([1, 1, 2, 5, 7]),0),"Should be 0"


    def testCount_3(self):
        self.assertEqual((count_paths([7,7,7,7,7])), 16),"Should be 16"


    def testCount_4(self):
        self.assertEqual((count_paths([])), 0),"Should be 0"

    def testCount_5(self):
        self.assertEqual((count_paths([2,7,9,4,5,6])), 2),"Should be 2"


if __name__ == '__main__':
    unittest.main()


from Ejercicio_2 import input
import unittest


class TestRandomized(unittest.TestCase):

    def testRandomizedSet_1(self):
        self.assertEqual(input([["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],[[], [1], [2], [2], [1], [1], [2], [2]]]),[None, True, False, True, 1, True, False, 2])

    def testRandomizedSet_2(self):
        self.assertTrue(input([["RandomizedSet","remove", "insert","getRandom"],[[], [1], [1],[1]]]),[None, False, True, 1])

    def testRandomizedSet_3(self):
        self.assertTrue(input([["RandomizedSet","insert", "remove","remove","insert","getRandom"],[[], [1], [1],[1],[5],[5]]]),[None, True, True,False,True ,5])

    def testRandomizedSet_4(self):
        self.assertTrue(input([["RandomizedSet","insert","insert","insert","insert","getRandom"],[[], [1], [2],[3],[1],[1]]]),[None, True, True,True,False,1])

    def testRandomizedSet_5(self):
        self.assertTrue(input([["RandomizedSet","insert","remove","remove","insert","getRandom"],[[], [4], [3],[4],[3],[3]]]),[None, True, False,True,True,3])

if __name__ == '__main__':
    unittest.main()

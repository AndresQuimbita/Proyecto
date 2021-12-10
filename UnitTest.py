from Ejercicio_2 import RandomizedSet
import unittest


class TestRandomized(unittest.TestCase):

    def testRandomizedSet_1(self):
        t1 = RandomizedSet()
        self.assertEqual(t1.insert(1),t1.remove(2),t1.insert(2),t1.getRandom(),t1.remove(1),t1.insert(2),t1.getRandom()),"Should be [null, true, false, true, Rand(1-2), true, false, 2]"


    def testRandomizedSet_2(self):
        t2 = RandomizedSet()
        self.assertTrue(t2.getRandom(),t2.remove(3),t2.insert(1),t2.getRandom()),"Should be [null, false, false, true, 1]"



if __name__ == '__main__':
    unittest.main()

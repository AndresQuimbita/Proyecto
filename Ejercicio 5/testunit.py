from Ejercicio5 import Determinar_ganador
import unittest

class TestNumerosRotados(unittest.TestCase):
    def testNumeroRotados1(self):
        self.assertEqual(Determinar_ganador(3),True)
        
    def testNumeroRotados2(self):
        self.assertEqual(Determinar_ganador(2),True)
        
    def testNumeroRotados3(self):
        self.assertEqual(Determinar_ganador(1),False)
        
    def testNumeroRotados4(self):
        self.assertEqual(Determinar_ganador(-1),0)   
        
    def testNumeroRotados5(self):
        self.assertEqual(Determinar_ganador(5),True)
        
    def testNumeroRotados6(self):
        self.assertEqual(Determinar_ganador(4),False) 
        

unittest.main()         
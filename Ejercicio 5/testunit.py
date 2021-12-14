from Ejercicio5 import Determinar_ganador
import unittest

class TestDeterminarGanador(unittest.TestCase):
    def testDeterminarGanador1(self):
        self.assertEqual(Determinar_ganador(3),True)
        
    def testDeterminarGanador2(self):
        self.assertEqual(Determinar_ganador(2),True)
        
    def testDeterminarGanador3(self):
        self.assertEqual(Determinar_ganador(1),False)
        
    def testDeterminarGanador4(self):
        self.assertEqual(Determinar_ganador(-1),0)   
        
    def testDeterminarGanador5(self):
        self.assertEqual(Determinar_ganador(5),True)
        
    def testDeterminarGanador6(self):
        self.assertEqual(Determinar_ganador(4),False) 
        

unittest.main()         
from Ejercicio3 import encontrar_duplicados
import unittest


class CasosVerificar(unittest.TestCase):

    def testEncontrar_duplicado1(self):
        self.assertEqual(encontrar_duplicados([1, 2, 2, 3]),2)
        
    def testEncontrar_duplicado2(self):
        self.assertEqual(encontrar_duplicados([1, 1, 3, 3]),1)    
        
    def testEncontrar_duplicado3(self):
        self.assertEqual(encontrar_duplicados([1, 1]),1)    
                
    def testEncontrar_duplicado4(self):
        self.assertEqual(encontrar_duplicados([2,2,1]),2)
        
    def testEncontrar_duplicado5(self):
        self.assertEqual(encontrar_duplicados([]),None)        
        
    def testEncontrar_duplicado6(self):
        self.assertEqual(encontrar_duplicados([1,1,2,2,3,4,3,6]),1)   
              
    def testEncontrar_duplicado7(self):
        self.assertEqual(encontrar_duplicados([7]), None)             
                             
    def testEncontrar_duplicado8(self):
        self.assertEqual(encontrar_duplicados([7,6,5,4,3]), None)
                                     
unittest.main()                
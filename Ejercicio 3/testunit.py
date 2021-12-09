from Ejercicio3 import encontrar_duplicados
import unittest


class CasosVerificar(unittest.TestCase):

    def testArray_cuadratic1(self):
        self.assertEqual(encontrar_duplicados([1, 2, 2, 3]),2)
        
    def testArray_cuadratic2(self):
        self.assertEqual(encontrar_duplicados([1, 1, 3, 3]),1)    
        
    def testArray_cuadratic3(self):
        self.assertEqual(encontrar_duplicados([1, 1]),1)    
                
    def testArray_cuadratic4(self):
        self.assertEqual(encontrar_duplicados([2,2,1]),2)
        
    def testArray_cuadratic5(self):
        self.assertEqual(encontrar_duplicados([1,1,2,2,3,4,3,6]),1)   
            
    def testArray_cuadratic6(self):
        self.assertEqual(encontrar_duplicados([7,4,2,1,3,4,7,6]),7)   
                             
unittest.main()                
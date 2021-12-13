from Ejercicio11 import retornar_resultado
import unittest

class TestNumerosRotados(unittest.TestCase):
    def testNumeroRotados1(self):
        self.assertEqual(retornar_resultado(2),["11","69","88","96"])
        
    def testNumeroRotados2(self):
        self.assertEqual(retornar_resultado(1),["0","1","8"])        
        
    def testNumeroRotados3(self):
        self.assertEqual(retornar_resultado(0),[""])     
        
    def testNumeroRotados4(self):
        self.assertEqual(retornar_resultado(-2),[])
    
    def testNumeroRotados5(self):
        self.assertEqual(retornar_resultado(4),['1001', '6009', '8008', '9006', '1111', '6119',
                                                  '8118', '9116', '1691', '6699', '8698', '9696',
                                                  '1881', '6889', '8888', '9886', '1961', '6969', '8968', '9966'])
    def testNumeroRotados6(self):
        self.assertEqual(retornar_resultado(3),['101', '609', '808', '906', '111', '619', '818',
                                                  '916', '181', '689', '888', '986'])       
                             
    def testNumeroRotados7(self):
        self.assertEqual(retornar_resultado(4.3),[""]) 
        
unittest.main()        
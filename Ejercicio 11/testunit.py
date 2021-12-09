from Ejercicio11 import definirNumero_rotado
import unittest

class TestNumerosRotados(unittest.TestCase):
    def testNumeroRotados1(self):
        self.assertEqual(definirNumero_rotado(2),["11","69","88","96"])
        
    def testNumeroRotados2(self):
        self.assertEqual(definirNumero_rotado(1),["0","8","1"])        
        
    def testNumeroRotados3(self):
        self.assertEqual(definirNumero_rotado(0),[""])     
        
    def testNumeroRotados4(self):
        self.assertEqual(definirNumero_rotado(-2),[""])
    
    def testNumeroRotados5(self):
        self.assertEqual(definirNumero_rotado(4),["1111", "6119", "8118", "9116", "1691",
                                                   "6699", "8698", "9696", "1881", "6889", "8888",
                                                   "9886", "1961", "6969", "8968", "9966"])
    def testNumeroRotados6(self):
        self.assertEqual(definirNumero_rotado(3),["101", "609", "808", "906", "181", "689",
                                                  "888", "986", "111", "619", "818", "916"])                            
    def testNumeroRotados7(self):
        self.assertEqual(definirNumero_rotado(4.3),[""]) 
        
unittest.main()        
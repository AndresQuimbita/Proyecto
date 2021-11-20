# Ejercicio 11
#11. Given an integer $n$, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.
#A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

#Example 1:

#Input: n = 2
#Output: ["11","69","88","96"]
#Example 2:

#Input: n = 1
#Output: ["0","1","8"]

import unittest
class Nodo:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None      
class Stack:
    def __init__(self):
        self.size=0
        self.top=self
        self.siguiente_nodo=None
        
    def push(self,data):
        nuevo_nodo=Nodo(data)
        nuevo_nodo.nextval=self.top
        self.top=nuevo_nodo
        self.size +=1

def definirNumero_rotado(valor_ingreso):
    if valor_ingreso > 1:
        resultado=[]
        valores_medios=list(definirNumero_rotado(valor_ingreso-2))
        for i in valores_medios:
            resultado.append("1" + i + "1")
            resultado.append("6" + i + "9")
            resultado.append("8" + i + "8")
            resultado.append("9" + i + "6")
        resultado=sorted(resultado)   
    
    elif valor_ingreso==1:
        resultado=[]
        valores_medios=list(definirNumero_rotado(valor_ingreso-1))
        for i in valores_medios:
            resultado.append("0")
            resultado.append("8")            
            resultado.append("1")
        resultado=sorted(resultado)    
    elif valor_ingreso==0:
        return [""]
    return resultado
                      
def almacenar_Stack(lista):
    Resultado_valores=Stack()
    for i in lista:
        Resultado_valores.push(i)
    print(lista)    
      
class TestNumbers(unittest.TestCase):
    def test_strobogrammatic(self):
        self.assertAlmostEquals(definirNumero_rotado(2),['11', '69', '88', '96'])



if __name__ == '__main__':
    unittest.main()
       

validar2=definirNumero_rotado(2)
almacenar_Stack(validar2)    
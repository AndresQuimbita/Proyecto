"""
Ejercicio 11. 
Given an integer , return all the strobogrammatic numbers that are of length n. You may return the answer in any order.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]

Explicacion: Para la solucion de este problema consideramos los numeros de 0 hasta 9, de esta lista de numeros, los unicos que al ser rotados 180 grados son el mismo valor o 
cambian de valor son los numeros 0,1,6,8,9. Por lo que para valores mayores que uno, determinamos los valores medios utilizando recursion para las siguientes iteraciones para 
crear los numeros rotados, en cada iteracion se agregan los 4 numeros. Ya que en cuando el valor comienza en 1 siempre va a terminar en el mismo valor 1, de igual manera con los valores
que comienzan con 6 terminaran con 9, los valores que comienzan con 8 terminaran con el mismo valor 8 y el valor de inicio 9 terminara con el valor 6. Cuando valor_ingreso vale 1, es decir
los numeros strombogramaticos de este tamaño son unicamente el 0, el 8 y el 1. Cuando valor_ingreso toma el valor de 0 no hay numeros strombogramaticos por lo que se retorna la lista vacia
"""


def definirNumero_rotado(valor_ingreso):
    resultado=[]
    if type(valor_ingreso) is int:
        if valor_ingreso > 1:
            valores_medios=(definirNumero_rotado(valor_ingreso-2))
            for i in valores_medios:
                resultado.append("1" + i + "1")
                resultado.append("6" + i + "9")
                resultado.append("8" + i + "8")
                resultado.append("9" + i + "6")  
        elif valor_ingreso==1:
            valores_medios=(definirNumero_rotado(valor_ingreso-1))
            for i in valores_medios:
                resultado.append("0")
                resultado.append("8")            
                resultado.append("1")
        elif valor_ingreso==0:
            return [""]
        else:
            return [""]
        return resultado
    else: 
        return [""]

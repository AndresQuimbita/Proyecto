"""
Ejercicio 3:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1

Explicacion: Para la solucion tomamos los casos bases cuando un arreglo tiene un unico elemento no existira un valor repetido
y el caso cuando el arreglo esta vacio donde retornamos None, cuando no se cumplen estos dos casos, recorremos mediante un for
desde 1 hasta el valor de longitud y comparamos mediante un if si la posicion actual de i ya se encuentra en el arreglo, 
si se cumple este if retornamos este valor en este punto de i. 
"""

def encontrar_duplicados(arreglo):
    longitud=len(arreglo)
    if longitud== 0:
        return None
    elif longitud== 1:
        return None
    else:
        for i in range(1,longitud):
            if arreglo[i] == arreglo[i-1]:
                return arreglo[i]
    return None

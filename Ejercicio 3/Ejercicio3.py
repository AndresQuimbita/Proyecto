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

Explicacion: Para la solucion se utilizaran una lista la cual es ingresada por el usuario y todos los procesos seran realizaran sobre esta lista, 
de igua manera dos variables iniciados en la posicion inicial del arrelgo, mediante un ciclo while verificamos la existencia del valor estatico contra 
los valores que se van a recorrer en la variable estatica. Si el valor del puntero estatico  es igual al valor que esta en ese punto del puntero que
recorre sabemos que dicho valor es el que se repite, por lo que cambiamos a Falso nuestra variable booleana y se retorna el valor donde si se cumplio el 
valor de if. Mientras que el puntero estatico sea diferente  al puntero que recorre el arreglo va a seguir asignando el siguiente 
valor del arreglo hasta el final donde retornamos el valor que se repite. 

"""

def encontrar_duplicados(arreglo):
    puntero_estatico = arreglo[0]
    puntero_aRecorrido = arreglo[0]
    verificar_existencia=True
    while verificar_existencia:
        puntero_estatico = arreglo[puntero_estatico]
        puntero_aRecorrido = arreglo[arreglo[puntero_aRecorrido]]
        if puntero_estatico == puntero_aRecorrido:
            verificar_existencia=False
    puntero_estatico = arreglo[0]
    while puntero_estatico != puntero_aRecorrido:
        puntero_estatico = arreglo[puntero_estatico]
        puntero_aRecorrido = arreglo[puntero_aRecorrido]
    return puntero_aRecorrido    
    
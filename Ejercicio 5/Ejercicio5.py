"""
Ejercico 5:

A Fibonacci tree is a binary tree created using the order function order(n):

order(0) is the empty tree.
order(1) is a binary tree with only one node.
order(n) is a binary tree that consists of a root node with the left subtree as order(n - 2) and the right subtree as order(n - 1).
Alice and Bob are playing a game with a Fibonacci tree with Alice staring first. On each turn, a player selects a node and removes that node and its subtree. 
The player that is forced to delete root loses.

Given the integer n, return true if Alice wins the game or false if Bob wins, assuming both players play optimally.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
Input: n = 3
Output: true
Explanation:
Alice takes the node 1 in the right subtree.
Bob takes either the 1 in the left subtree or the 2 in the right subtree.
Alice takes whichever node Bob doesn't take.
Bob is forced to take the root node 3, so Bob will lose.
Return true because Alice wins.

Explicion: Utilizando el Principio de Colon el cual establece que para ramas que se unen en un vertice
se puede reemplazar dichas ramas por un tallo no ramificado de su misma longitud. Por lo que determinamos
que para la solucion determinamos las soluciones en el principio de Colon es decir, una lista compuesto de cero y uno. Mediante un
for recorremos los posibles resultados para valores ingresados de tal manera que cumpla la condicion de:
SG(N)=(SG(N-1)+1) (SG(N-2)+1). Y para resultados en el que SG=0 debemos retornar False y para SG=1 debemos 
retornar True
"""

def Determinar_ganador(valor_ingresado):
    resultados=[0,1]
    for i in range(2,valor_ingresado):
        resultados[i%2]=(resultados[(i-1)%2])^(resultados[(i-2)%2])
    return resultados[(valor_ingresado-1)%2]>0


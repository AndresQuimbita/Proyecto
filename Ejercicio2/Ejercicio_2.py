"""
para este ejercicio se considero el uso de diccionarios para asi lograr el tiempo de complejidad, se usaron 4 funciones, 
la de insert,remove, get random y la de input para lograr el input con arreglos


"""


import random


class RandomizedSet:
    def __init__(self, list):
        self.d = {}
        self.list = list

    def insert(self, val):
        if str(val) in self.d.keys():
            return False
        else:
            self.d[str(val)] = val
            self.list.append(val)
            return True

    def remove(self, val):
        if str(val) in self.d.keys():
            del self.d[str(val)]
            self.list.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        if len(self.d.keys()) == 0:
            return None
        random.seed(2)
        rndmnum = random.choice(self.list)
        return rndmnum


def input(A, B):
    output = [None for i in range(len(A))]
    init_set = None
    for i in range(len(A)):
        if A[i] == "RandomizedSet":
            init_set = RandomizedSet(B[i])
            output[i] = None
        if A[i] == "insert":
            if not init_set:
                output[i] = False
            else:
                output[i] = init_set.insert(B[i][0])

        if A[i] == "remove":
            if not init_set:
                output[i] = False
            else:
                output[i] = init_set.remove(B[i][0])
        if A[i] == "getRandom":
            if not init_set:
                output[i] = False
            else:
                output[i] = init_set.getRandom()
    return output

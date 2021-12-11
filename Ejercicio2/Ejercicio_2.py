# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

class RandomizedSet:
    def __init__(self):
        self.d = {}

    def insert(self, val):

        if self.d:
            for i in range(len(self.d.keys())):
                if str(val) in self.d.keys():
                    return print(False)
                else:
                    self.d[str(val)] = val
                    return print(True)
        else:
            self.d[str(val)] = val
            return print(True)

    def remove(self, val):
        if self.d:
            for i in range(len(self.d.keys())):
                if str(val) in self.d.keys():
                    del self.d[str(val)]
                    return print(True)
                else:
                    return print(False)
        else:
            return print(False)

    def getRandom(self):
        if len(self.d.keys()) == 0:
            return False
        rndmnum = random.randint(1,len(self.d.keys()))
        return print(rndmnum)







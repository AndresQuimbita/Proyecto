# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

class RandomizedSet:
    def __init__(self):
        self.d = {}

    def insert(self, val):

        if self.d:
            if str(val) in self.d.keys():
                return False
            else:
                self.d[str(val)] = val
                return True
        else:
            self.d[str(val)] = val
            return True

    def remove(self, val):
        if self.d:
            if str(val) in self.d.keys():
                del self.d[str(val)]
                return True
            else:
                return False
        else:
            return False

    def getRandom(self):
        if len(self.d.keys()) == 0:
            return False
        rndmnum= random.choice(list(self.d.keys()))
        return rndmnum







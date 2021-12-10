import random

class RandomizedSet:

    def __init__(self):
        self.list = []

    def insert(self, val):
        if self.list:
            for i in range(len(self.list)):
                if val in self.list:
                    return print(False)
                else:
                    self.list.append(val)
                    return print(True)
        else:
            self.list.append(val)
            return print(True)

    def remove(self, val):
        if self.list:
            for i in range(len(self.list)):
                if val in self.list:
                    self.list.remove(val)
                    return print(True)
                else:
                    return print(False)
        else:
            return print(False)

    def getRandom(self):
        if len(self.list) == 0:
            return print(False)
        rndmnum = self.list[random.randint(0,len(self.list))-1]
        return print(rndmnum)







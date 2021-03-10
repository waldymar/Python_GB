from abc import ABC, abstractmethod

class Cloth(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consum(self):
        pass

    def __add__(self, other):
        return self.consum + other.consum

class Coat(Cloth):

    @property
    def consum(self):
        return self.param / 6.5 + 0.5

class Costume(Cloth):

    @property
    def consum(self):
        return 2 * self.param + 0.3

c1 = Coat(100)
c2 = Costume(2)
print(round(c1 + c2))
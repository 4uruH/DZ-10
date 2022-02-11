from abc import abstractmethod


class Cloth:

    @abstractmethod
    def consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Cloth):
    def __init__(self, hight):
        self.hight = hight

    @property
    def consumption(self):
        return self.hight * 2 + 0.3


a = Coat(56)
b = Costume(183)
print(round(a.consumption, 2))
print(round(b.consumption, 2))
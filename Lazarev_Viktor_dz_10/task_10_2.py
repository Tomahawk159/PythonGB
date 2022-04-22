from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.value / 6.5 + 0.5, 1)


class Costume(Clothes):
    @property
    def calculation(self):
        return round(self.value * 2 + 0.3, 1)


coat = Coat(48)
costume = Costume(1.75)

print('Расход ткани на пальто: ', coat.calculation)
print('Расход ткани на костюм: ', costume.calculation)

total_calculate = coat.calculation + costume.calculation

print('Общий расход ткани: ', total_calculate)

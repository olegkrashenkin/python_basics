from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        """Объявляем размер одежды"""
        self.size = size

    @staticmethod
    def sum_clothes_cons(suit=0, coat=0, dress=0):
        """
        Расчет общего расхода ткани
        :param suit: размер пиджака
        :param coat: размер пальто
        :param dress: размер платья
        """
        return Suit(suit).clothes_cons + Coat(coat).clothes_cons + Dress(dress).clothes_cons

    @abstractmethod
    def clothes_cons(self):
        pass


class Suit(Clothes):
    @property
    def clothes_cons(self):
        """Расчет расхода ткани для пошива костюма"""
        if not self.size:
            return 0
        return round(2 * self.size + 0.3, 2)


class Coat(Clothes):
    @property
    def clothes_cons(self):
        """Расчет расхода ткани для пошива пальто"""
        if not self.size:
            return 0
        return round(self.size / 6.5 + 0.5, 2)


class Dress(Clothes):
    @property
    def clothes_cons(self):
        """Расчет расхода ткани для пошива платья"""
        if not self.size:
            return 0
        return round(self.size / 4 + 0.8, 2)


print(
    f'Расход ткани на пошив костюма: {Suit(177).clothes_cons}\n'
    f'Расход ткани на пошив пальто: {Coat(46).clothes_cons}\n'
    f'Расход ткани на пошив платья: {Dress(42).clothes_cons}\n'
    f'Общий расход ткани: {Suit.sum_clothes_cons(177, 46, 42)}'
)

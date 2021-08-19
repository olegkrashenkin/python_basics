class Cell:
    def __init__(self, cell):
        if not isinstance(cell, int):
            exit('Только целое число!')
        self.cell = cell

    def make_order(self, line):
        if not isinstance(line, int):
            exit('Только целое число!')
        icon = '*\t'
        return ''.join([f'{icon * (self.cell % line)}' if i == self.cell // line
                        else f'{icon * line}\n' for i in range(self.cell // line + 1)])

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        try:
            if other.cell > self.cell:
                return exit('Делитель больше делимого!')
            return self.cell // other.cell
        except ZeroDivisionError:
            exit('На ноль делить нельзя!')

    def __truediv__(self, other):
        """
        Классическое округление результата:
        n.4(и <) = n, n.5(и >) = n+1
        Если результат меньше нуля - округление до единицы.
        """
        try:
            if (self.cell / other.cell) < 1:
                return 1
            else:
                return round(self.cell / other.cell)
        except ZeroDivisionError:
            exit('На ноль делить нельзя!')


c_1 = Cell(56)
c_2 = Cell(10)
print(
    f'Клетка №1: {c_1.cell}\nКлетка №2: {c_2.cell}\nСложение: {c_1 + c_2}'
      f'\nВычитание: {c_1 - c_2}\nКлассическое деление с округлением: {c_1 / c_2}'
      f'\nЦелая часть от деления: {c_1 // c_2}\nУмножение: {c_1 * c_2}\n'
      f'Метод make_order() со значением 6,\nдля клетки №1:\n{c_1.make_order(6)}\n'
      f'Метод make_order() со значением 3,\nдля клетки №2:\n{c_2.make_order(3)}'
)

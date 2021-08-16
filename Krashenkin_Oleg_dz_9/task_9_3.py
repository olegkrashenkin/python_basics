class Worker:
    def __init__(self, n, s, p, w, b):
        """
        :param n: Имя
        :param s: Фамилия
        :param p: Должность
        :param w: Оклад
        :param b: Бонус
        """
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"оклад": f'{w}', "бонус": f'{b}'}


class Position(Worker):
    def get_full_name(self):
        """
        :return: Возвращает полное имя сотрудника
        """
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        """
        :return: Возвращает полный доход сотрудника (оклад + бонус)
        """
        return f'Доход: {sum(int(i) for i in self._income.values())}\u20BD'


wrkr = Position('Сергей', 'Петров', 'Сварщик', 25000, '4000')
print(f'Имя: {wrkr.name}\n'
      f'Фамилия: {wrkr.surname}\n'
      f'Должность: {wrkr.position}\n'
      f'Доход: {wrkr._income}')
print(wrkr.get_full_name())
print(wrkr.get_total_income())
from random import randrange


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = ''
        for sublist in self.matrix_list:
            for num in sublist:
                result += f'{num}\t'
            result += f'\n'
        return result

    def __add__(self, other):
        return Matrix([num_1 + num_2 for num_1, num_2 in zip(sublist_1, sublist_2)]
                      for sublist_1, sublist_2 in zip(self.matrix_list, other.matrix_list))

    def __sub__(self, other):
        return Matrix([num_1 - num_2 for num_1, num_2 in zip(sublist_1, sublist_2)]
                      for sublist_1, sublist_2 in zip(self.matrix_list, other.matrix_list))

    def __eq__(self, other):
        if self.matrix_list == other.matrix_list:
            return True
        return False

    def __ne__(self, other):
        if self.matrix_list == other.matrix_list:
            return False
        return True

    def __mul__(self, other):
        return Matrix([num_1 * num_2 for num_1, num_2 in zip(sublist_1, sublist_2)]
                      for sublist_1, sublist_2 in zip(self.matrix_list, other.matrix_list))

    def __floordiv__(self, other):
        for i in other.matrix_list:
            if 0 not in i:
                return Matrix([num_1 // num_2 for num_1, num_2 in zip(sublist_1, sublist_2)]
                              for sublist_1, sublist_2 in zip(self.matrix_list, other.matrix_list))
            return exit('Деление без остатка не сработало т.к. нельзя поделить')

    def __truediv__(self, other):
        for i in other.matrix_list:
            if 0 not in i:
                return Matrix([round(num_1 / num_2, 1) for num_1, num_2 in zip(sublist_1, sublist_2)]
                              for sublist_1, sublist_2 in zip(self.matrix_list, other.matrix_list))
            return exit('На ноль делить нельзя!')


sep = '-' * 30
print(f'\nПрограмма создает 2 матрицы со значениями от 1 до 10\n'
      f'для проверки перегруженных операторов.\n{sep}')
line = int(input('Количество строк в матрицах: '))
column = int(input('Количество столбцов в матрицах: '))
mtx_1 = Matrix([[randrange(1, 10) for i in range(line)] for i_ in range(column)])
mtx_2 = Matrix([[randrange(1, 10) for i in range(line)] for i_ in range(column)])
print(
    f'{sep}\n№1:\n{mtx_1}\n№2:\n{mtx_2}\n{sep}\n'
    f'№1 + №2:\n{mtx_1 + mtx_2}\n№1 - №2:\n{mtx_1 - mtx_2}\n№1 * №2:\n{mtx_1 * mtx_2}'
    f'\n№1 / №2:\n{mtx_1 / mtx_2}\n№1 // №2:\n{mtx_1 // mtx_2}\n№1 == №1:\n{mtx_1 == mtx_1}'
    f'\n№1 == №2:\n{mtx_1 == mtx_2}\n№1 != №1:\n{mtx_1 != mtx_1}\n№1 != №2:\n{mtx_1 != mtx_2}'
)

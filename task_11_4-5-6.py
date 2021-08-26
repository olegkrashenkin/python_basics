from colorama import Back, Fore, Style
from datetime import datetime
from re import search


def obj_valid(obj):
    while True:
        tmp = input(f'{obj.tech_param} - Все верно? (Y/N): ')
        if tmp == 'Y':
            return obj
        elif tmp == 'N':
            return None


def choice_valid(input_, *args):
    while True:
        a = input(f'{input_}')
        if a.isdigit():
            a = int(a)
            if a in args:
                return a


class Warehouse:
    l_sep = '- ' * 5
    r_sep = ' -' * 5

    @staticmethod
    def menu():
        sep = '* ' * 19
        print(f'{sep}\n*\t\t', end='')
        print(Back.WHITE, Fore.BLACK + '"Склад Оргтехники" ' + Style.RESET_ALL, end='')
        print(f'\t\t*\n*\t(1)Посмотреть наличие товара\t*\n*\t(2)Принять товар\t\t\t\t*\n'
              f'*\t(3)Отгрузить товар\t\t\t\t*\n*\t(4)Выход\t\t\t\t\t\t*\n{sep}')
        menu = choice_valid('Введите номер операции: ', 1, 2, 3, 4)
        if menu == 4:
            exit('Программа завершена!')
        elif menu == 2:
            Warehouse.add_product()
        elif menu == 1:
            Warehouse.in_stock()
        elif menu == 3:
            Warehouse.rm_product()

    @staticmethod
    def add_product():
        flag = True
        dev = choice_valid('(1)Принтер, (2)Сканер, (3)МФУ: ', 1, 2, 3)
        manufacturer = input('Производитель: ')
        model = input('Модель: ')
        a = {1: 'Printer', 2: 'Scanner', 3: 'AiO'}
        _ = [a[dev], manufacturer, model]
        product_code = f'{_[0][0]}{_[1][:2]}{_[1][-1]}{_[2][:2]}{_[2][-1]}'
        with open('vendor_code.txt', 'r', encoding='utf-8') as f:
            for i in f:
                i = i.split('|')
                if i[0] == product_code:
                    info = i[1]
                    flag = False
                    break
        if flag:
            t_ = {1: Printer, 2: Scanner, 3: AiO}
            info = t_[dev].mk_obj(manufacturer, model).tech_param
        count = int(input('Количество поступившего товара: '))
        date_tmp = search(r'^(\d{4})-(\d+)-(\d+)\s((?:\d+:){2}\d+)', str(datetime.now()))
        date = f'{date_tmp.group(3)}.{date_tmp.group(2)}.{date_tmp.group(1)}-{date_tmp.group(4)}'
        if flag:
            with open('database.txt', 'a', encoding='utf-8') as f:
                f.write(f'{count:>05}|{product_code}|{date}|\n')
            with open('vendor_code.txt', 'a', encoding='utf-8') as f:
                f.write(f'{product_code}|{info}|\n')
        else:
            with open('database.txt', 'r+', encoding='utf-8') as f:
                x = 0
                for i in f:
                    x += 1
                    if i.split('|')[1] == product_code:
                        num = int(i.split('|')[0])
                        break
                f.seek((x - 1) * 35)
                f.write(f'{num + count:>05}|{product_code}|{date}|\n')
        print(Fore.GREEN + f'{Warehouse.l_sep}Готово{Warehouse.r_sep}\n' + Style.RESET_ALL)
        return Warehouse.menu()

    @staticmethod
    def in_stock():
        _ = {1: 'P', 2: 'S', 3: 'A'}
        head_ = {1: 'Принтеры', 2: 'Сканеры', 3: 'МФУ'}
        choice = (choice_valid('(1)Принтеры, (2)Сканеры, (3)МФУ: ', 1, 2, 3))
        _ = _[choice]
        print(Fore.YELLOW + f'{Warehouse.l_sep}{head_[choice]}{Warehouse.r_sep}')
        with open('database.txt', 'r', encoding='utf-8') as d:
            with open('vendor_code.txt', 'r', encoding='utf-8') as v:
                count = 1
                for i in d:
                    i = i.split('|')
                    for i_ in v:
                        if i[1][0] == _:
                            i_ = i_.split('|')
                            s = i_[1].split(',')
                            i_ = search(r'^\W+(\w+)\W+(\w+)\W+(\w+)', str(s))
                            print(f'{count:>04}. Производитель: {i_.group(2)}\n'
                                  f'\t  Модель: {i_.group(3)}\n'
                                  f'\t  Наличие: {int(i[0])} шт.\n'
                                  f'\t  Дата изменения: {i[2]}\n')
                            count += 1
                            break
                        break
        print(Style.RESET_ALL)
        return Warehouse.menu()

    @staticmethod
    def rm_product():
        dev = choice_valid('(1)Принтер, (2)Сканер, (3)МФУ: ', 1, 2, 3)
        manufacturer = input('Производитель: ')
        model = input('Модель: ')
        a = {1: 'Printer', 2: 'Scanner', 3: 'AiO'}
        _ = [a[dev], manufacturer, model]
        product_code = f'{_[0][0]}{_[1][:2]}{_[1][-1]}{_[2][:2]}{_[2][-1]}'
        date_tmp = search(r'^(\d{4})-(\d+)-(\d+)\s((?:\d+:){2}\d+)', str(datetime.now()))
        date = f'{date_tmp.group(3)}.{date_tmp.group(2)}.{date_tmp.group(1)}-{date_tmp.group(4)}'
        with open('vendor_code.txt', 'r', encoding='utf-8') as v:
            for i in v:
                i = i.split('|')
                if i[0] == product_code:
                    with open('database.txt', 'r+', encoding='utf-8') as d:
                        x = 0
                        for i_ in d:
                            x += 1
                            if i_.split('|')[1] == product_code:
                                num = int(i_.split('|')[0])
                                break
                        count = int(input('Количество отгружаемого товара: '))
                        num = num - count
                        if num < 0:
                            print(Fore.RED + 'Нет столько товара в наличии!\n' + Style.RESET_ALL)
                            return Warehouse.menu()
                        d.seek((x - 1) * 35)
                        d.write(f'{num:>05}|{product_code}|{date}|\n')
                        print(Fore.GREEN + f'{Warehouse.l_sep}Готово{Warehouse.r_sep}\n' + Style.RESET_ALL)
                        return Warehouse.menu()
            print(Fore.RED + 'Такого товара нет в базе!\n' + Style.RESET_ALL)
            return Warehouse.menu()


class OfficeEquip:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year


class Printer(OfficeEquip):
    def __init__(self, manufacturer, model, year, print_tech, color):
        super().__init__(manufacturer, model, year)
        self.tech_param = ['Printer', self.manufacturer, self.model, self.year, print_tech, color]

    @classmethod
    def mk_obj(cls, manufacturer, model):
        while True:
            year = input('Год выпуска: ')
            print_tech_ = {1: 'laser', 2: 'ink'}
            print_tech = print_tech_[choice_valid('(1)Лазерный, (2)Струйный: ', 1, 2)]
            color_ = {1: 'color', 2: 'mono'}
            color = color_[choice_valid('(1)Цветной, (2)Ч/Б: ', 1, 2)]
            new_obj = cls(manufacturer, model, year, print_tech, color)
            if obj_valid(new_obj):
                return new_obj


class Scanner(OfficeEquip):
    def __init__(self, manufacturer, model, year, type_, dpi):
        super().__init__(manufacturer, model, year)
        self.tech_param = ['Scanner', self.manufacturer, self.model, self.year, type_, dpi]

    @classmethod
    def mk_obj(cls, manufacturer, model):
        while True:
            year = input('Год выпуска: ')
            type__ = {1: 'flatbed', 2: 'broaching', }
            type_ = type__[choice_valid('(1)Планшетный, (2)Протяжный: ', 1, 2)]
            dpi = input('Разрешение (dpi): ')
            new_obj = cls(manufacturer, model, year, type_, dpi)
            if obj_valid(new_obj):
                return new_obj


class AiO(OfficeEquip):
    def __init__(self, manufacturer, model, year, print_tech, color, dpi):
        super().__init__(manufacturer, model, year)
        self.tech_param = ['AiO', self.manufacturer, self.model, self.year, print_tech, color, dpi]

    @classmethod
    def mk_obj(cls, manufacturer, model):
        while True:
            year = input('Год выпуска: ')
            print_tech_ = {1: 'laser', 2: 'ink'}
            print_tech = print_tech_[choice_valid('1 - Лазерный, 2 - Струйный: ', 1, 2)]
            color_ = {1: 'color', 2: 'mono'}
            color = color_[choice_valid('1 - Цветной, 2 - Ч/Б: ', 1, 2)]
            dpi = input('Разрешение (dpi): ')
            new_obj = cls(manufacturer, model, year, print_tech, color, dpi)
            if obj_valid(new_obj):
                return new_obj


Warehouse.menu()

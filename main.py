from colorama import Back, Style, Fore
from random import choice, randint
from time import sleep
from os import system, name
from progress.spinner import MoonSpinner


def playground(field_):
    pgnd = field_.copy()
    _ = [i for i in pgnd.values()]
    cell_already_been = []
    count = 0
    while count != 13:
        ch_num = choice(_)
        if ch_num not in cell_already_been:
            pgnd[ch_num] = '👻'
            cell_already_been.append(ch_num)
            count += 1
    return pgnd


def game(player_1, player_2):
    Field.show_playground(p_num)
    while total_rate != 13:
        player_1.step()
        if total_rate != 13:
            player_2.step()
        else:
            break
    if player_1.rate > player_2.rate:
        print(f'Победил {player_1.name}!')
    else:
        print(f'Победил {player_2.name}!')


class Field:
    field = {f'{i + 1:>02}': f'{i + 1:>02}' for i in range(50)}
    fill_field = playground(field)

    @classmethod
    def show_playground(cls, type_game):
        global total_rate
        count = 1
        system('cls' if name == 'nt' else 'clear')
        for i in cls.field.values():
            if count % 5 != 0:
                if i[0] == 'f':
                    print(Back.LIGHTGREEN_EX, Fore.BLACK + f'|{i[1:]}| ' + Style.RESET_ALL, end='')
                    count += 1
                elif i[0] == 's':
                    print(Back.LIGHTRED_EX, Fore.BLACK + f'|{i[1:]}| ' + Style.RESET_ALL, end='')
                    count += 1
                else:
                    print(Back.LIGHTWHITE_EX, Fore.BLACK + f'|{i}| ' + Style.RESET_ALL, end='')
                    count += 1
            else:
                if i[0] == 'f':
                    print(Back.LIGHTGREEN_EX, Fore.BLACK + f'|{i[1:]}| ' + Style.RESET_ALL)
                    count += 1
                elif i[0] == 's':
                    print(Back.LIGHTRED_EX, Fore.BLACK + f'|{i[1:]}| ' + Style.RESET_ALL)
                    count += 1
                else:
                    print(Back.LIGHTWHITE_EX, Fore.BLACK + f'|{i}| ' + Style.RESET_ALL)
                    count += 1
        if type_game == 1:
            print(Fore.LIGHTGREEN_EX + f'{p_1.name}: {p_1.rate}' + Style.RESET_ALL, end='')
            print(' | ', end='')
            print(Fore.LIGHTRED_EX + f'{c_1.name}: {c_1.rate}' + Style.RESET_ALL)
            total_rate = p_1.rate + c_1.rate
        elif type_game == 2:
            print(Fore.LIGHTGREEN_EX + f'{p_1.name}: {p_1.rate}' + Style.RESET_ALL, end='')
            print(' | ', end='')
            print(Fore.LIGHTRED_EX + f'{p_2.name}: {p_2.rate}' + Style.RESET_ALL)
            total_rate = p_1.rate + p_2.rate
        else:
            print(Fore.LIGHTGREEN_EX + f'{c_1.name}: {c_1.rate}' + Style.RESET_ALL, end='')
            print(' | ', end='')
            print(Fore.LIGHTRED_EX + f'{c_2.name}: {c_2.rate}' + Style.RESET_ALL)
            total_rate = c_1.rate + c_2.rate


class Player:
    already_been = []

    def __init__(self, name, id, rate=0):
        self.name = name
        self.id = id
        self.rate = rate


class Human(Player):

    def step(self):
        while total_rate != 13:
            print(f'Ходит {self.name}')
            while True:
                try:
                    cell_number = int(input('В какой номер пойдем?: '))
                except ValueError:
                    print(Fore.LIGHTRED_EX + 'Такого номера в отеле нет! (1 - 50)' + Style.RESET_ALL)
                else:
                    if 1 <= cell_number <= 50:
                        _ = f'{cell_number:>02}'
                        if _ not in Player.already_been:
                            cell_number = _
                            break
                        else:
                            print(Fore.LIGHTRED_EX + 'Этот номер уже проверили!' + Style.RESET_ALL)
                    elif cell_number == 5555:
                        exit('ЗАПАСНЫЙ ВЫХОД')
                    else:
                        print(Fore.LIGHTRED_EX + 'Такого номера в отеле нет! (1 - 50)' + Style.RESET_ALL)
            Player.already_been.append(cell_number)
            if Field.fill_field[cell_number] == '👻':
                Field.field[cell_number] = f'{self.id}👻'
                self.rate += 1
                Field.show_playground(p_num)
                print(f'{self.name} поймал призрака в номере {cell_number}!')
            else:
                Field.field[cell_number] = f'{self.id}🤷'
                Field.show_playground(p_num)
                print(f'{self.name} разбудил постояльца из номера {cell_number}!')
                break


class Computer(Player):
    def step(self):
        while total_rate != 13:
            bar = MoonSpinner(f'Ходит {self.name}: ', max=len(Field.field))
            sleep(0.2)
            for _ in Field.field:
                bar.next()
                sleep(0.02)
            bar.finish()
            sleep(0.2)
            while True:
                _ = randint(1, 50)
                _ = f'{_:>02}'
                if _ not in Player.already_been:
                    cell_number = _
                    break
            Player.already_been.append(cell_number)
            if Field.fill_field[cell_number] == '👻':
                Field.field[cell_number] = f'{self.id}👻'
                self.rate += 1
                Field.show_playground(p_num)
                print(f'{self.name} поймал призрака в номере {cell_number}!')
            else:
                Field.field[cell_number] = f'{self.id}🤷'
                Field.show_playground(p_num)
                print(f'{self.name} разбудил постояльца из номера {cell_number}!')
                break


p_num = 3  # выбор игры: 1 - игрок/компьютер, 2 - игрок/игрок, 3 - компьютер/компьютер(демо)
total_rate = 0

if p_num == 1:
    system('cls' if name == 'nt' else 'clear')
    name_ = input(f'Введите имя первого игрока: ')
    p_1 = Human(name_, 'f')
    c_1 = Computer('Компьютер', 's')
    game(p_1, c_1)
elif p_num == 2:
    system('cls' if name == 'nt' else 'clear')
    name_ = input(f'Введите имя первого игрока: ')
    p_1 = Human(name_, 'f')
    name_ = input(f'Введите имя второго игрока: ')
    p_2 = Human(name_, 's')
    game(p_1, p_2)
else:
    c_1 = Computer('Компьютер 1', 'f')
    c_2 = Computer('Компьютер 2', 's')
    game(c_1, c_2)
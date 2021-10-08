from colorama import Back, Style, Fore
from random import choice, randint
from time import sleep
from os import system, name
from progress.bar import ChargingBar


def show_field(loc_dict):
    field_color = [Back.LIGHTYELLOW_EX, Back.LIGHTGREEN_EX, Back.LIGHTBLUE_EX,
                   Back.LIGHTMAGENTA_EX, Back.LIGHTCYAN_EX, Back.LIGHTRED_EX,
                   Back.LIGHTWHITE_EX]
    cnt = 1
    system('cls' if name == 'nt' else 'clear')
    for k, v in loc_dict.items():
        if cnt % 10 != 0:
            print(field_color[color - 1], Fore.BLACK + f'|{v}|' + Style.RESET_ALL, end='')
            cnt += 1
        else:
            print(field_color[color - 1], Fore.BLACK + f'|{v}| ' + Style.RESET_ALL)
            cnt += 1
    print(f'Игрок: {player_hit} из 10\t\t\t Компьютер: {computer_hit} из 10')


def player_turn(fill_field_, default_field_):
    global player_hit
    while player_hit != 10:
        print('Ход Игрока')
        while True:
            try:
                cell_number = int(input('Введите номер ячейки: '))
            except ValueError:
                print(Fore.LIGHTRED_EX + 'Такой ячейки нет! (0 - 99)' + Style.RESET_ALL)
            else:
                if 0 <= cell_number <= 99:
                    _ = f'{cell_number:>02}'
                    if _ not in already_been:
                        cell_number = _
                        break
                    else:
                        print(Fore.LIGHTRED_EX + 'Эта ячейка уже открыта!' + Style.RESET_ALL)
                elif cell_number == 5555:
                    exit('ЗАПАСНЫЙ ВЫХОД')
                else:
                    print(Fore.LIGHTRED_EX + 'Такой ячейки нет! (0 - 99)' + Style.RESET_ALL)
        already_been.append(cell_number)
        if fill_field_[cell_number] == '**':
            default_field_[cell_number] = '**'
            show_field(default_field_)
            print(f'Игрок открыл ячейку {cell_number}\n'
                  f'Она оказалась заполненной!')
            player_hit += 1
        else:
            default_field_[cell_number] = '__'
            show_field(default_field_)
            print(f'Игрок открыл ячейку {cell_number}\n'
                  f'Она оказалась пустой!')
            break


def computer_turn(fill_field_, default_field_):
    global computer_hit
    while computer_hit != 10:
        bar = ChargingBar('Ход Компьютера: ', max=len(default_field))
        sleep(0.2)
        for _ in default_field:
            bar.next()
            sleep(0.01)
        bar.finish()
        sleep(0.2)
        while True:
            _ = randint(0, 99)
            _ = f'{_:>02}'
            if _ not in already_been:
                cell_number = _
                break
        already_been.append(cell_number)
        if fill_field_[cell_number] == '**':
            default_field_[cell_number] = '**'
            show_field(default_field_)
            print(f'Компьютер открыл ячейку {cell_number}\n'
                  f'Она оказалась заполненной!')
            computer_hit += 1
        else:
            default_field_[cell_number] = '__'
            show_field(default_field_)
            print(f'Компьютер открыл ячейку {cell_number}\n'
                  f'Она оказалась пустой!')
            break


default_field = {f'{i:>02}': f'{i:>02}' for i in range(100)}
field = default_field.copy()
_ = [i for i in field.values()]
cell_already_been = []
count = 0
while count != 25:
    ch_num = choice(_)
    if ch_num not in cell_already_been:
        field[ch_num] = '**'
        cell_already_been.append(ch_num)
        count += 1
player_hit = 0
computer_hit = 0
already_been = []
system('cls' if name == 'nt' else 'clear')
while True:
    print('\nВыберите цвет игрового поля (', end='')
    print(Back.LIGHTYELLOW_EX, Fore.BLACK + '1 ' + Style.RESET_ALL, end='')
    print(Back.LIGHTGREEN_EX, Fore.BLACK + '2 ' + Style.RESET_ALL, end='')
    print(Back.LIGHTBLUE_EX, Fore.BLACK + '3 ' + Style.RESET_ALL, end='')
    print(Back.LIGHTMAGENTA_EX, Fore.BLACK + '4 ' + Style.RESET_ALL, end='')
    print(Back.LIGHTCYAN_EX, Fore.BLACK + '5 ' + Style.RESET_ALL, end='')
    print(Back.LIGHTRED_EX, Fore.BLACK + '6 ' + Style.RESET_ALL, end='')
    print(Back.LIGHTWHITE_EX, Fore.BLACK + '7 ' + Style.RESET_ALL, end='')
    try:
        color = int(input('): '))
    except ValueError:
        print(Fore.RED + 'Выберите номер палитры!' + Style.RESET_ALL)
    else:
        if 0 <= color <= 7:
            break
        else:
            print(Fore.RED + 'Выберите номер палитры!' + Style.RESET_ALL)
show_field(default_field)
while computer_hit != 10:
    player_turn(field, default_field)
    if player_hit != 10:
        computer_turn(field, default_field)
    else:
        break
if computer_hit > player_hit:
    print(f'На {step} ходу победил Компьютер!')
else:
    print(f'На {step} ходу победил Игрок!')
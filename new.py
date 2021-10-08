from colorama import Back, Style, Fore
from random import choice


def show_field(field_dict):
    count = 0
    for k, v in field_dict.items():
        if k[0] == 'p':
            print(Back.LIGHTWHITE_EX, Fore.BLACK + f'|{v}| ' + Style.RESET_ALL, end='')
            count += 1
        else:
            if count == 5:
                print(f'\t\t', end='')
                print(Back.LIGHTBLUE_EX, Fore.BLACK + f'|{v}| ' + Style.RESET_ALL, end='')
                count = 0
            elif k[0] == 'e' and count != 3:
                print(Back.LIGHTBLUE_EX, Fore.BLACK + f'|{v}| ' + Style.RESET_ALL, end='')
                count += 1
            else:
                print(Back.LIGHTBLUE_EX, Fore.BLACK + f'|{v}| ' + Style.RESET_ALL)
                count = 0
    print('Player 1\t\t\t\t\t\t\tPlayer 2')


field = {}
count = 1
for i in range(51):
    if count % 6 != 0:
        field[f'p{i + 1:>02}'] = f'{i + 1:>02}'
        count += 1
    else:
        for _ in range(i):
            field[f'e{_ + 1:>02}'] = f'{_ + 1:>02}'
        if i != 50:
            field[f'p{i + 1:>02}'] = f'{i + 1:>02}'
            count = 2
full_field = field.copy()
field_key_list = [i for i in full_field.keys()]
cell_already_been = []
count_p = 0
count_e = 0
while count_p + count_e != 30:
    choice_val = choice(field_key_list)
    if choice_val not in cell_already_been:
        if choice_val[0] == 'p' and count_p != 15:
            full_field[choice_val] = '**'
            cell_already_been.append(choice_val)
            count_p += 1
        elif choice_val[0] == 'e' and count_e != 15:
            full_field[choice_val] = '**'
            cell_already_been.append(choice_val)
            count_e += 1

show_field(full_field)

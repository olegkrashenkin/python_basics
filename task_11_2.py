class MyZeroErr(Exception):
    pass


while True:
    a = input('Введите делимое: ')
    try:
        a = int(a)
    except ValueError:
        print('Некорректный ввод!')
    else:
        break
while True:
    b = input('Введите делитель: ')
    try:
        b = int(b)
        if int(b) == 0:
            raise MyZeroErr
    except (ValueError, MyZeroErr):
        print('Некорректный ввод!')
    else:
        break
print(f'{a} : {b} = {round(a/b)}')
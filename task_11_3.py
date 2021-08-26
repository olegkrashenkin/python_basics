some_list = []
while True:
    a = input('Введите число: ')
    if a == 'stop':
        break
    try:
        a = int(a)
    except ValueError:
        print('Можно вводить только числа!')
    else:
        some_list.append(a)
print(some_list)

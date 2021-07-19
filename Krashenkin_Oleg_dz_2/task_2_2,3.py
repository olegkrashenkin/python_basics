weather = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']
id_before = id(weather)
for i in weather:
    if i.isdigit() or i.replace('+', '').isdigit():
        if len(i) == 1:
            print(f'"0{i}"', end=' ')
        elif i[0] == '+':
            print(f'"+0{i[1:]}"', end=' ')
        else:
            print(f'"{i}"', end=' ')
    elif i == weather[-1]:  # Не придумал как можно лучше перенести строку в конце предложения
        print(i)
    else:
        print(i, end=' ')
id_after = id(weather)
print('Сравнение id до и после выполнения кода =', id_before == id_after)

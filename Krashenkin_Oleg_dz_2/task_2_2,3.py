my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']
id_before = id(my_list)
i = 0
while i < len(my_list):
    if my_list[i].isdigit():
        my_list[i] = my_list[i].rjust(2, '0')
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 2
    elif my_list[i][:1] == '+':
        my_list[i] = '+' + my_list[i][1:].rjust(2, '0')
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 2
    i += 1
result = ' '.join(my_list)
while True:
    temp = result.find(' " ')
    if temp != -1:
        result = result[:temp + 2] + result[temp + 3:]
        temp = result.find(' " ')
        result = result[:temp] + result[temp + 1:]
    else:
        break
print(result)
id_after = id(my_list)
print('Сравнение id до и после выполнения кода =', id_before == id_after)
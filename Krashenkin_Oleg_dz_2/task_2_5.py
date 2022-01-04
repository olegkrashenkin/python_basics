price_list = [57.8, 46.51, 97, 15.3, 34, 87.15, 14.12, 22.9, 61, 11.17]
# Часть A:
for i in price_list:
    i = str(i)
    if i == str(price_list[-1]):  # Как и в задании 2_2,3 не придумал как можно лучше сделать перенос строки
        if '.' in i:
            if '.' in i[-2:]:
                print(f'{i.replace(".", " руб ")}0 коп')
            else:
                print(f'{i.replace(".", " руб ")} коп')
        else:
            print(f'{i} руб 00 коп')
    elif '.' in i:
        if '.' in i[-2:]:
            print(f'{i.replace(".", " руб ")}0 коп', end=', ')
        else:
            print(f'{i.replace(".", " руб ")} коп', end=', ')
    else:
        print(f'{i} руб 00 коп', end=', ')
# Часть B:
id_before = id(price_list)
price_list.sort()
print(price_list)
id_after = id(price_list)
print('Сравнение id до и после сортировки =', id_before == id_after)
# Часть C:
sort_price = sorted(price_list, reverse=True)
# Часть D:
print(sorted(price_list, reverse=True)[4::-1])

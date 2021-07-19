# Создать вручную список, содержащий цены на товары (10–20 товаров).
price_list = [57.8, 46.51, 97, 15.3, 34, 87.15, 14.12, 22.9, 61, 11.17]

# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули,
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
def price_format(some_list):
    result = ''
    for i in some_list:
        i = str(i)
        if '.' in i:
            if '.' in i[-2:]:
                result += i.replace('.', ' руб ') + '0 коп, '
            else:
                result += i.replace('.', ' руб ') + ' коп, '
        else:
            result += i + ' руб 00 коп, '
        if i == str(some_list[-1]):
            result = result[:-2] + result[-1].rstrip()
    return result


print('Задание А:')
print(price_format(price_list))

# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
print('Задание B:')
id_before = id(price_list)
print(sorted(price_list))
id_after = id(price_list)
print('Сравнение id до и после сортировки =', id_before == id_after)

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
sort_price_v1 = sorted(price_list, reverse=True)
# или
sort_price_v2 = price_list.copy()
sort_price_v2.sort()
sort_price_v2.reverse()

# Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print('Задание D:')
print(sorted(price_list, reverse=True)[4::-1])

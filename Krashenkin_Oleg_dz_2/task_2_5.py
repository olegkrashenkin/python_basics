price_list = [57.8, 46.51, 97, 15.3, 34, 87.15, 14.12, 22.9, 61, 11.17]


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


print(price_format(price_list))
id_before = id(price_list)
print(sorted(price_list))
id_after = id(price_list)
print('Сравнение id до и после сортировки =', id_before == id_after)
sort_price_v1 = sorted(price_list, reverse=True)
# или
sort_price_v2 = price_list.copy()
sort_price_v2.sort()
sort_price_v2.reverse()
print(sorted(price_list, reverse=True)[4::-1])

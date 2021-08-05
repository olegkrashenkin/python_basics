from sys import argv


def show_slice(start, end=None):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if f.read()[f.seek((int(start) - 1) * 11):].split('\n') != ['']:
            if end is None:
                try:
                    a = f.read()[f.seek((int(start) - 1) * 11):end].split('\n')
                    a.remove('')
                    for i in a:
                        print(float(i))
                except ValueError:
                    exit('Неверный ввод!\n'
                         'Пример: show_sales.py <номер записи начала просмотра>')
            else:
                try:
                    a = f.read()[f.seek((int(start) - 1) * 11):f.seek(int(end) * 11)].split('\n')
                    a.remove('')
                    for i in a:
                        print(float(i))
                except ValueError:
                    exit('Неверный ввод!\n'
                         'Пример: show_sales.py <номер записи начала просмотра> '
                         '<номер записи конца просмотра>')
        else:
            exit('Записи с таким номером не существует!')


try:
    start = argv[1]
except IndexError:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        a = f.read().split('\n')
        a.remove('')
        for i in a:
            print(float(i))
else:
    try:
        stop = argv[2]
    except IndexError:
        show_slice(start)
    else:
        show_slice(start, stop)

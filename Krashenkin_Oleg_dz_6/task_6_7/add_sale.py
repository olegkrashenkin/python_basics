from sys import argv

try:
    if argv[1].replace(',', '').replace('.', '').isdigit() and len(argv[1]) <= 8:
        with open('bakery.csv', 'a', encoding='utf-8') as f:
            f.write(f"{float(argv[1].replace(',', '.')):<010}\n")
    else:
        exit('Неверный ввод!\n'
             'Пример: add_sale.py <числовое значение, максимально 8 символов>')
except IndexError:
    exit('Неверный ввод!\n'
         'Пример: add_sale.py <числовое значение, максимально 8 символов>')

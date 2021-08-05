from sys import argv

try:
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        if argv[1].isdigit() and argv[2].replace(',', '').replace('.', '').isdigit() and len(argv[2]) <= 8:
            if f.read()[f.seek((int(argv[1]) - 1) * 11):].split('\n') != ['']:
                f.seek((int(argv[1]) - 1) * 11)
                f.write(f"{float(argv[2].replace(',', '.')):<010}\n")
            else:
                exit('Записи с таким номером не существует!')
        else:
            exit('Неверный ввод!\n'
                 'Пример: change_sale.py <номер записи> <новое значение, максимально 8 символов>')
except IndexError:
    exit('Неверный ввод!\n'
         'Пример: change_sale.py <номер записи> <новое значение, максимально 8 символов>')

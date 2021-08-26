from re import compile


class Date:
    def __init__(self, date):
        if compile(r'^(\d{2}-){2}\d{4}$').match(date):
            self.date = date
        else:
            exit('Некорректный формат даты!\nПример: "ДД-ММ-ГГГГ"')

    @classmethod
    def __trans_int(cls, obj_date):
        return map(int, obj_date.split('-'))

    @staticmethod
    def validator(obj):
        d, m, y = obj.__trans_int(obj.date)
        if d in range(1, 32) and m in range(1, 13) and 0 < y <= 9999:
            return f'Дата {obj.date} корректна!'
        else:
            exit('Некорректные данные!\nДень: 1-31\nМесяц: 1-12\nГод: 1-9999')


some_date_object = Date('16-12-2012')
print(Date.validator(some_date_object))
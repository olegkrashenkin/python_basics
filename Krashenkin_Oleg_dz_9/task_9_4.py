from colorama import Back, Style, Fore


class Car:
    def __init__(self, speed, color, name, is_police):
        """
        :param speed: Скорость (Целое число)
        :param color: Цвет
        :param name: Имя
        :param is_police: Машина полицейская? (True/False)
        """
        if isinstance(speed, int) and isinstance(is_police, bool):
            self.speed = speed
            self.is_police = is_police
        else:
            exit('Неверный ввод!')
        self.color = color
        self.name = name

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}км/ч'

    def go(self):
        return f'Автомобиль {self.name} движется.'

    def stop(self):
        return f'Автомобиль {self.name} остановился.'

    def turn(self, direction):
        """
        :param direction: Укажите направление (север, юг, запад, восток)
        """
        if direction in ('север', 'юг', 'запад', 'восток'):
            return f'Автомобиль {self.name} повернул на {direction}.'
        else:
            exit('Неверный ввод!')

    def horn(self, count):
        """
        Включение сигнала на автомобиле
        :param count: Сколько раз сработает сигнал (Целое число)
        """
        if isinstance(count, int):
            c = count
            while c != 0:
                if self.is_police:
                    print(Back.LIGHTRED_EX, Fore.BLUE + 'ВИУ-ВИУ-ВИУ ', end='')
                    print(Back.LIGHTBLACK_EX, Fore.LIGHTWHITE_EX + '((*)) ', end='')
                    print(Back.BLUE, Fore.LIGHTRED_EX + 'КРЯ-КРЯ-КРЯ ', end='')
                    print(Style.RESET_ALL)
                    if c != 1:
                        print('.' * 33)
                else:
                    print(f'Автомобиль {self.name} делает БИ-БИ=)')
                c -= 1
        else:
            exit('Неверный ввод!')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name} превысил скорость на {self.speed - 60}км/ч!'
        else:
            return f'Скорость автомобиля {self.name} - {self.speed}км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} превысил скорость на {self.speed - 40}км/ч!'
        else:
            return f'Скорость автомобиля {self.name} - {self.speed}км/ч'


class PoliceCar(Car):
    pass


t = TownCar(80, 'зеленый', 'Жигуль', False)
print(f'Имя: {t.name}\n'
      f'Цвет: {t.color}\n'
      f'Скорость: {t.speed}\n'
      f'Машина полицейская?: {t.is_police}')
print(t.go())
print(t.show_speed())
print(t.turn('север'))
t.horn(1)
print(t.stop())
print('-' * 40)
w = WorkCar(30, 'оранжевый', 'КАМАЗ', False)
print(f'Имя: {w.name}\n'
      f'Цвет: {w.color}\n'
      f'Скорость: {w.speed}\n'
      f'Машина полицейская?: {w.is_police}')
print(w.go())
print(w.show_speed())
print(w.turn('запад'))
w.horn(2)
print(w.stop())
print('-' * 40)
p = PoliceCar(120, 'хаки', 'УАЗ', True)
print(f'Имя: {p.name}\n'
      f'Цвет: {p.color}\n'
      f'Скорость: {p.speed}\n'
      f'Машина полицейская?: {p.is_police}')
print(p.go())
p.horn(3)
print(p.show_speed())
print(p.turn('восток'))
print(p.stop())

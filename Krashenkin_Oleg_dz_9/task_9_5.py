class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашом {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером {self.title}'


stationery = Stationery()
print(stationery.draw())
pen = Pen('BiG')
print(pen.draw())
pencil = Pencil('Луч')
print(pencil.draw())
handle = Handle('ГаММа')
print(handle.draw())

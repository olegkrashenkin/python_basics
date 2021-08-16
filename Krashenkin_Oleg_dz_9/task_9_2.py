class Road:
    def __init__(self, length, width):
        """
        :param l: длина дороги
        :param w: ширина дороги
        """
        self._length = length
        self._width = width

    def new_road(self, weight, thickness):
        """
        :param weight: масса асфальта для покрытия 1кв/м дороги асфальтом, толщиной в 1см
        :param thickness: толщины полотна в см
        :return: масса асфальта, необходимого для покрытия всей дороги
        """
        return f'{round(self._length * self._width * weight * thickness / 1000)}т.'


# Пример из методички: 20м * 5000м * 25кг * 5см = 12500т.
r = Road(20, 5000)
print(r.new_road(25, 5))

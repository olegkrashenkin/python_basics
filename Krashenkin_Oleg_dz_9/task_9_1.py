from time import sleep
from colorama import Back, Style, Fore


class TrafficLight:
    __color = [Back.LIGHTRED_EX, Back.LIGHTYELLOW_EX, Back.LIGHTGREEN_EX]

    def running(self, r_delay=7, y_delay=2, g_delay=5):
        while True:
            print(self.__color[0], Fore.BLACK + 'STOP')
            sleep(r_delay)
            print(self.__color[1] + ' READY')
            sleep(y_delay)
            print(self.__color[2] + ' GO-O-O-O!')
            sleep(g_delay)
            print(Style.RESET_ALL)


tl = TrafficLight()
tl.running(1, 1, 1)

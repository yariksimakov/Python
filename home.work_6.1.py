from time import sleep
from itertools import cycle

class Traffic_light:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for color, second in cycle(self.__color):
            print(color)
            sleep(second)

start = Traffic_light((('Red', 7), ('Yellow', 2), ('Green', 5)))
start.running()
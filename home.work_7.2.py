# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, el):
        self.param = el

    @abstractmethod
    def summ(self):
        print('Hello')


class Coat(Clothes):

    @property
    def consumption(self):
        return self.param / 6.5 + 0.5

    def summ(self):
        return "Coat"


class Costume(Clothes):

    @property
    def consumption(self):
        return self.param * 2 + 0.3

    def summ(self):
        return "Costume"


if __name__ == '__main__':
    start = Coat(26)
    print(start.consumption, start.summ())
    start = Costume(10)
    print(start.consumption, start.summ())

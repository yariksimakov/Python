class Road:
    def __init__(self, length, width):
        self.__a = length
        self.__b = width
    def wigtht(self):
        return self.__a * self.__b * 30 * 0.1

print('{} kg'.format(Road(20, 2).wigtht()))

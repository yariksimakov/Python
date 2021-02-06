class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        return self.count - other.count if self.count - other.count > 0 \
                else "Разность количества ячеек двух клеток меньше нуля,"

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, quant):
        return '\n'.join(['* ' * quant for i in range(self.count // quant)]) \
               + '\n' + '* ' * (self.count % quant)


if __name__ == '__main__':
    start_1 = Cell(43)
    start_2 = Cell(20)
    print(start_1.make_order(5))
    print(start_1 + start_2)
    print(start_2.make_order(8))
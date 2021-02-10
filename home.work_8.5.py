# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, count):
        self.number = count

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


if __name__ == "__main__":
    start_1 = Complex(15)
    start_2 = Complex(41)
    print(start_1 + start_2)
    print(start_1 * start_2)
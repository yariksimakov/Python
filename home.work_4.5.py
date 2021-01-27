# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
def my_f(num_1, num_2):
    return num_1 * num_2

print(reduce(my_f, [el for el in range(100, 1001) if el % 2 == 0]))
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_pow(x, y):
    return x ** y
print(my_pow(int(input('enter number: ')), int(input('enter number: '))))

""" second way """

def my_func(x, y):
    """ Может работать с любым значение y"""
    i = 0
    if y <= 0:
        factor = 1
        while i > y:
            i -= 1
            factor /= x
        else:
            factor = 1
    else:
        factor = x
        while i < y:
            i += 1
            factor *= x
    return factor
print(my_func(2, -2))

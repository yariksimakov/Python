# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


user_list = input("enter two numbers separated by a space: ")
user_list = user_list.split()
var_1 = int(user_list[0])
var_2 =  int(user_list[1])
def division(number_1, number_2):
    try:
        result_1 = number_1 / number_2
        result_2 = number_2 / number_1
        return round(result_1, 2), round(result_2, 2)
    except ZeroDivisionError:
        return('you entered the number zero, division is not possible')
print(division(var_1, var_2))
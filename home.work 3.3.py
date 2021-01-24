# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    user_max_1 = my_list.pop(my_list.index(max(my_list)))
    user_max_2 = my_list.pop(my_list.index(max(my_list)))
    return user_max_1 + user_max_2
print(my_func(0,0,0))




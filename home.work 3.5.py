# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
#
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

result = 0
x = True
while x == True:
    my_list = input('enter number, if want to go out dial end: ')
    my_list = my_list.split()
    my_sum = 0
    for index in my_list:
        if index == 'end':
            x = False
            break
        my_sum += int(index)
    result += my_sum
print(result)

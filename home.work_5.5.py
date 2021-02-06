# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('5.5.txt', 'w', encoding='utf-8') as file:
    num = '1 2 3 4 5'
    file.write('Enter number: ' + num + '\n')
    num_sum = map(int, num.split())
    num_sum = sum(num_sum)
    file.write('Summa numbers: ' + str(num_sum))

# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('home.work_5.2.txt') as file:
    my_list = file.readlines()
print(f'Всего строк: {len(my_list)}')
count = 0
for line in my_list:
    if line == '\n':
        continue
    else:
        count += 1
        print(line.split(), f'Количество слов: {len(line.split())}')
print('Количество строк, не щитая пустых: {}'.format(count))
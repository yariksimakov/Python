# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
with open('home.work_5.4.txt', encoding='utf-8') as file:
    lines = file.readlines()

with open('home.work_5.4-new .txt', 'w', encoding='utf-8') as file:
    russian = ['Один', 'Два', 'Три', 'Четыре']
    for num, i in enumerate(lines):
        line = i.split(' - ')
        line[0] = russian[num]
        line.insert(1, ' - ')
        file.writelines(line)

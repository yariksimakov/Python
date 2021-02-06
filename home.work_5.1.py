# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.


with open('home.work_5.1.txt', 'w') as file:
    result = []
    while True:
        user_text = input('Enter text: ')
        if user_text == '':
            break
        result.append(user_text + '\n')
    file.writelines(result)
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open('5.7.txt') as file:
    lines = file.readlines()
print(lines)

succes_dict = {}
average_profit = []
loser_dict = {}
for index in lines:
    user_list = index.split()
    profit = int(user_list[2]) - int(user_list[3])
    if profit > 0:
        average_profit.append(profit)
        succes_dict[user_list[0]] = profit
    else:
        loser_dict[user_list[0]] = abs(profit)

average_profit = sum(average_profit) / len(average_profit)
result_list = [succes_dict, '\n', {'Average profit: ': round(average_profit)}]
# \n Это я пытался перенести текст на другую строку но потерпел фиаско

result_list_loser = {'Loser firm: ': loser_dict}
print(result_list_loser)

with open('5.7.json', 'w') as file:
    json.dump(result_list, file)
    json.dump(result_list_loser, file)
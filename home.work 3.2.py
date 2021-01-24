# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def person_data(**kwargs):
    return kwargs

user_tuple = person_data(name = input('name: '), surname = input('surname: '),
                year_of_birth = int(input('year_of_birth: ')),
                current_city = input('current_city: '),
                email = input('email: '), telephon = int(input('telephon: ')))

print(user_tuple)


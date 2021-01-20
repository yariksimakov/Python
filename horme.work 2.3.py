#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и dict.


while True:
    user = int(input('Enter number: '))
    if user >= 1 and user <= 12:
        break
    else:
        print(" not number")
if user >= 1 and user <=2 or user == 12:
    print('Winter')
elif user >= 3 and user <= 5:
    print('Spring')
elif user > 5 and user < 9:
    print("Summer")
else:
    print('Autumn')
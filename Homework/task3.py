"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
winter_month = [12, 1, 2]
spring_month = [3, 4, 5]
summer_month = [6, 7, 8]
autumn_month = [9, 10, 11]
Seasons_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
while True:
    try:
        user_input = int(input('Введите номер месяца>>> '))
        if user_input in range(1, 12):
            break
        else:
            print('Введен несуществующий месяц. Введите значение от 1 до 12')
    except ValueError:
        print('Некорректный ввод')
print('from lists: ', end='')
if user_input in winter_month:
    print('winter')
elif user_input in spring_month:
    print('spring')
elif user_input in summer_month:
    print('summer')
else:
    print('autumn')

for season, months in Seasons_dict.items():
    if user_input in months:
        print('from dictionary:', season)


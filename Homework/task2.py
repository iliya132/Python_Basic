"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def print_user_data(first_name, last_name, father_name, birth_year, town, email, phone_number):
    print(f'{last_name} {first_name} {father_name}:\n{birth_year}b.y.\nLive in {town}\nContact info:\n{email}\n' +
          f'{phone_number}')


f_name = input('Введите имя>>> ')
l_name = input('Введите фамилию>>> ')
fath_name = input('Введите отчество>>> ')
b_year = input('Введите дату рождения>>> ')
town = input('Введите город проживания>>> ')
mail = input('Введите Email>>> ')
p_number = input('Введите номер телефона>>> ')
print_user_data(first_name=f_name,
                last_name=l_name,
                father_name=fath_name,
                birth_year=b_year,
                town=town,
                email=mail,
                phone_number=p_number)

"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(first_float, second_float):
    """Функция выполняет операцию деления первого числа на второе"""
    try:
        result = first_float / second_float
        return result
    except ZeroDivisionError:
        print('Деление на нуль невозможно')


def read_float(message):
    try:
        user_input = float(input(message))
        return user_input
    except ValueError:
        return


first = None
second = None
while first is None:
    first = read_float('Введите первое число')
while second is None:
    second = read_float('Введите второе число')

print(f'{first} devided by {second} = {divide(first, second)}')

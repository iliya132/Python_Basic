"""Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    return x ** y


def my_func2(x, y):
    if y > 0:
        is_degree_positive = True
    else:
        is_degree_positive = False
    degree_counter = my_abs(y) - 1  # -1 т.к. pow_result инициируется значением x
    pow_result = x
    while degree_counter > 0:
        degree_counter -= 1
        pow_result *= x
    if not is_degree_positive:
        pow_result = 1 / pow_result
    return pow_result


def my_abs(i):
    if i < 0:
        i *= -1
    return i


num = 2
degree = -3
print(f'{num}^{degree} = ** func {my_func(num, degree)}')
print(f'{num}^{degree} = my_func2 {my_func2(num, degree)}')

num = 2
degree = 3
print(f'{num}^{degree} = ** func {my_func(num, degree)}')
print(f'{num}^{degree} = my_func2 {my_func2(num, degree)}')

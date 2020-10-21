"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_min(*args):
    if len(args) > 0:
        min = args[0]
        for i in args:
            if i < min:
                min = i
        return min
    else:
        return


def my_func(first, second, third):
    minimum = my_min(first, second, third)
    return first + second + third - minimum


a = 5
b = 9
c = 6
print(f'sum of biggest integers of [{a} {b} {c}] is {my_func(a,b,c)}')

def my_reduce(func, list):
    """Возвращает результат вычислении функции над списком"""
    if len(list) == 0:
        return
    result = list[0]
    try:
        for i in range(1, len(list)):
            result = func(result, list[i])
        return result
    except ValueError:
        print('Неожиданное значение в списке. Допускается использование только чисел')
        return
    except ZeroDivisionError:
        print('Неверная математическая операция. Деление на ноль.')


def my_range(start, end, step=1):
    """Возвращает последовательность чисел начиная с start до end(не включительно) с шагом step"""
    while start < end:
        yield start
        start += step


def my_cycle(list):
    """Функция создаст бесконечный итератор, циклически возвращающий элементы объекта, поддерживающего итерирование.
    Цикличность заключается в том, что, после исчерпания элементов итерируемого объекта,
    проход по элементам начинается вновь."""
    if len(list) < 1:
        return
    i = 0
    while True:
        yield list[i]
        i += 1
        if i == len(list):
            i = 0


def my_enumerate(list, start_index = 0):
    for item in list:
        yield start_index, item
        start_index += 1



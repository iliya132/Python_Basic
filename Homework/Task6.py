from itertools import count
from itertools import cycle
from my_functions import my_range
from my_functions import my_cycle
"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""


#  а) итератор, генерирующий целые числа, начиная с указанного,
def my_range_with_itertools(start, end):
    for i in count(start, 1):
        if i >= end:
            break
        yield i


#  б) итератор, повторяющий элементы некоторого списка, определенного заранее.
def my_cycle_with_itertools(list, count):
    if count < 1:
        return
    for item in cycle(list):
        yield item
        count -= 1
        if count < 1:
            break

def my_cycle_func(list,count):  #реализовано с использованием самописной функции из my_functions.py
    if count < 1:
        return
    for item in my_cycle(list):
        yield item
        count -= 1
        if count < 1:
            break

print(list(my_range(3,10)))  # реализовано с использованием самописной функции из my_functions.py
print(list(my_cycle_func('ABC', 10)))   # реализовано с использованием самописной функции из my_functions.py
print(list(my_range_with_itertools(3,10)))  # реализовано с использованием itertools
print(list(my_cycle_with_itertools('ABC', 10)))  # реализовано с использованием itertools

from my_functions import my_reduce as reduce
"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

list = [itm for itm in range(100, 1001)
        if not itm & 1]
print(list)
product = reduce(lambda x,y: x*y, list)
print(product)
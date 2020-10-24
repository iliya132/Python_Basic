"""2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

def gen_list(list):
    new_list = [itm
                for id, itm
                in enumerate(list)
                if id != 0 and list[id] > list[id-1]]
    return new_list

inital_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(gen_list(inital_list))  #result [12, 44, 4, 10, 78, 123]
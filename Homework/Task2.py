"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой."""


class MyException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


def divide(a, b):
    if b == 0:
        raise MyException("На ноль делить нельзя")
    return a / b


input1 = input("Введите делимое: ")
input2 = input("Введите делитель: ")
try:
    x = float(input1)
    y = float(input2)
    print("result is ", divide(x, y))
except ValueError:
    print("Введено не число")
except MyException:
    print("Делить на ноль нельзя")

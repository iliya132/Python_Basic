"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Date:
    __day = 1
    __month = 1
    __year = 1900

    def __init__(self, date: str):
        try:
            self.__day, self.__month, self.__year = Date.parse_date(date)
            if not Date.is_valid(self.__day, self.__month, self.__year):
                raise ValueError("Задано некорректное значение даты")
        except ValueError:
            print(f"Cant parse date value from {date} string")

    @classmethod
    def parse_date(cls, date_str: str):
        items = date_str.split('-')
        day = int(items[0])
        month = int(items[1])
        year = int(items[2])
        return day, month, year

    @staticmethod
    def is_valid(day, month, year):
        max_days = 31
        if month in [4, 6, 9, 11]:
            max_days = 30
        if month == 2:
            max_days = 27
        if not year % 4 and month == 2:  # Весокосный год
            max_days = 28
        return 0 < day <= max_days and 0 < month < 13 and 0 < year < 9999

    def __str__(self):
        return f"{self.__day:02d}.{self.__month:02d}.{self.__year:04d}"


if __name__ == "__main__":
    assert Date.is_valid(7, 11, 2020)
    assert Date.is_valid(28, 2, 2020)
    assert not Date.is_valid(28, 2, 2019)
    assert Date.is_valid(30, 11, 2020)
    assert not Date.is_valid(31, 11, 2020)
    test_date = Date("07-11-2020")
    print(test_date)

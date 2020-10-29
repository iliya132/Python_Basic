"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

rus_numbers = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
               "seven": "семь", "eight": "восемь", "nine": "девять", "zero": "ноль"}

with open("Numbers.txt", "r", encoding="utf-8") as file:
    _ = open("Task4Result.txt", "w", encoding="utf-8")  # Очищаю файл
    for line in file.read().splitlines():
        with open("Task4Result.txt", "a", encoding="utf-8") as output:
            str_num = line.split(" - ")[0].lower()  # One
            int_num = line.split(" - ")[1]  # 1
            output.write(f'{rus_numbers[str_num]} - {int_num}\n')  # один - 1

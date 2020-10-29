"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""
from my_functions import my_enumerate
try:
    file = open("TestInput.txt", "r")
    lines = file.readlines()
    file.close()
    for num, line in my_enumerate(lines, 1):
        print(f'{num} строка - {len(line.split(" "))} слов')
except IOError:
    print("Не найден файл для чтения")
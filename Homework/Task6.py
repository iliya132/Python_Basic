"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

def get_first_number(text):
    """Метод ищет первое попавшееся целое число в строке.
    Если число прерывается символом - возвращает число
    Пример
    get_first_number("30(л) — 10(лаб)") == 30"""
    result = ''
    for char in text:
        if char.isdigit():
            result += char
        else:
            break
    if result.isdigit():
        return int(result)
    else:
        return


file = open("Task6Input.txt", "r", encoding="utf-8")
lines = file.read().splitlines()
file.close()

result = {}
for line in lines:
    # line - Информатика: 100(л) 50(пр) 20(лаб).
    header = line[:line.index(':')]  # Читаем слово до ':' - Информатика
    values = line[line.index(':') + 2: len(line)].split(' ')  # весь текст после ": " - 100(л) 50(пр) 20(лаб).
    hours_sum = sum([get_first_number(hours) for hours in values if get_first_number(hours) is not None])
    result.update({header: hours_sum})

print(result)

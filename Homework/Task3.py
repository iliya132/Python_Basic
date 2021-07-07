"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

file = open("Employees.txt", "r", encoding="UTF-8")
lines = file.read().splitlines()  # Читаю так что бы убрать \n
file.close()
print(lines)
print("Сотрудники с зарплатой ниже 20,000:")
for employee_info in [empl for empl in lines if int(empl.split(" ")[1]) < 20000]:
    print(employee_info)

salary_sum = sum([float(slr.split()[1]) for slr in lines])
print(f'Средняя зарплата - {salary_sum / len(lines)}')

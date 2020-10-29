"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

def calc_profit(gain, expenses):
    """Считаем прибыльность компании"""
    return gain-expenses


def calc_average_profit(companies):
    """Считает среднюю доходность компаний"""
    sum = 0
    count = 0
    for company in companies:
        current_company_profit = calc_profit(company['Gain'], company['Expenses'])
        if current_company_profit > 0:
            count += 1
            sum += current_company_profit
    if count != 0:
        return sum / count


companies_list = []
average_profit = {"Average_Profit": 0}
with open("Task7Input.txt", "r", encoding="utf-8") as input:
    lines = input.readlines()

for line in lines:
    company_info = line.split(' ')
    try:
        company = {"Name": company_info[0],
                   "Form": company_info[1],
                   "Gain": float(company_info[2]),
                   "Expenses": float(company_info[3]),
                   "Profit": calc_profit(float(company_info[2]), float(company_info[3]))}
        companies_list.append(company)
        print(f'Прибыль компании {company["Form"]} {company["Name"]} = '
              f'{calc_profit(company["Gain"], company["Expenses"])}')
    except ValueError:
        print("Не удалось распознать компанию")
average_profit["Average_Profit"] = calc_average_profit(companies_list)
print(f'Средняя прибыльность среди компаний - {average_profit["Average_Profit"]:.02f}')

result = (companies_list, average_profit)
with open("Task7Result.json", "w", encoding="UTF-8") as output:
    output.write(json.dumps(result, ensure_ascii=False))

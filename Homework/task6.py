"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и
словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). С
труктуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[

(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
characteristic_list = []
# Коллекция уникальных характеристик (не использовал set, т.к. он не сохраняет сортировку)
distinct_characteristics = []
good_id = 0
goods_list = []
# Опрашиваем характеристики товаров
while True:
    user_input = input('Введите характеристику товара (q для выхода)>>> ')
    if user_input == 'q':
        break
    characteristic_list.append(user_input)

# Удаляем дублирующиеся характеристики
for item in characteristic_list:  
    if item not in distinct_characteristics:
        distinct_characteristics.append(item)

while True:  # Опрашиваем товары
    user_input = input('Добавить товар? [y/n]')
    if user_input == 'n':
        break
    elif user_input != 'y':
        print('Не понял - попробуйте еще раз.')
        continue
    good_dict = {}
    for characteristic in distinct_characteristics:
        user_input = input(f'{characteristic}>>> ')
        try:  # если возможно преобразовать в число - преобразуем
            float_val = float(user_input)
            good_dict.update({characteristic: float_val})
        except ValueError:  # Иначе добавляем значение как есть
            good_dict.update({characteristic: user_input})
    good_id += 1
    goods_list.append((good_id, good_dict))

# создаем словарь
goods_dict = {}
for characteristic in distinct_characteristics:
    current_characteristic_values = []
    for item in goods_list:
        current_characteristic_values.append(item[1][characteristic])
    # Здесь можно было бы добавлять в качестве значения set, но подумал что это было бы не логично, т.к.
    # потом было бы проблематично соотносить значения с конкретным товаром
    goods_dict.update({characteristic: current_characteristic_values})
print('Сформированный словарь:')
print(goods_dict)

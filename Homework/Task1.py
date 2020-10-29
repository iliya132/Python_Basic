"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open("TaskResult.txt", "w") as file:
    while True:
        user_input = input("Введите любую строку>>>")
        if user_input == "":
            break
        file.write(f'{user_input}\n')

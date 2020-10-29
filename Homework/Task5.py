"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""


def file_sum(file):
        lines = file.read().splitlines()
        numbers = []
        try:
            for line in lines:
                for num in line.split(" "):
                    numbers.append(int(num))
        except ValueError:
            pass
        return sum(numbers)


res_file_name = "Task5Result.txt"
_ = open(res_file_name, "w")
while True:
    user_input = input('Введите числа, разделенные пробелами (q для выхода)>>> ')
    if user_input == 'q':
        break
    with open(res_file_name, "a") as output:
        output.write(f'{user_input}\n')

file = open(res_file_name, "r")
print(file_sum(file))



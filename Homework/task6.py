"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()."""


def int_func(some_text):
    return some_text.capitalize()


def int_func2(some_text: str):
    export_val = ''
    for item in some_text.split(' '):
        export_val += f'{int_func(item)} '
    return export_val[:-1]


print(int_func('test test test'))
print(int_func2('test test test'))

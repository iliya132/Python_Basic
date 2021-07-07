"""1. Реализовать класс Matrix (матрица). 
Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных 
в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы 
в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения 
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть 
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент 
первой строки первой матрицы складываем с первым элементом первой строки 
второй матрицы и т.д.
"""


class Matrix:
    __rows_count = 0
    __columns_count = 0

    def __init__(self, data):
        self.__matrix = data
        dimensions = self.__check_dimensions()
        self.__rows_count = dimensions[0]
        self.__columns_count = dimensions[1]

    def __str__(self):
        output = ''
        for y in self.__matrix:
            for x in y:
                output += f'{x} '
            output += '\n'
        return output[:len(output) - 2]  # Убираю последний \n

    def __add__(self, other):
        if self.__check_dimensions() != other.__check_dimensions():
            raise ArithmeticError("Матрицы имеют разную размерность. Сложение невозможно")
        new_matrix = []
        idx = 0
        idy = 0
        while idy < self.__rows_count:
            new_row = []
            while idx < self.__columns_count:
                new_row.append(self.__matrix[idy][idx] + other.__matrix[idy][idx])
                idx += 1
            new_matrix.append(new_row)
            idx = 0
            idy += 1
        return Matrix(new_matrix)

    def __check_dimensions(self):
        """Метод проверяет что матрица правильной размерности и представляет из себя прямоугольник
        возвращается количество строк и столбцов"""
        rows_count = len(self.__matrix)
        if rows_count < 1:
            return 0, 0
        columns_count = len(self.__matrix[0])
        for row in self.__matrix:
            if len(row) != columns_count:
                self.__matrix = None
                raise ValueError('Входящий аргумент не является матрицей')
        return rows_count, columns_count


if __name__ == "__main__":
    test_matrix1 = Matrix([[1, 2, 3, 4],
                           [1, 2, 3, 4],
                           [1, 2, 3, 4]])
    test_matrix2 = Matrix([[10, 11, 12, 13],
                           [13, 16, 19, 20],
                           [14, 25, 23, 24]])
    print(test_matrix1)
    print()
    print(test_matrix2)
    print()
    print(test_matrix1 + test_matrix2)
    """result:
        11 13 15 17 
        14 18 22 24 
        15 27 26 28
    """

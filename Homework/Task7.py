"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата."""

def ComplexOperation(func):
    def wrapper(self, other):
        if not isinstance(self, Complex) or not isinstance(other, Complex):
            raise ArithmeticError("В операции должны участвовать два комплексных числа")
        return func(self, other)
    return wrapper


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f'{self.a}{self.b}i'
        return f'{self.a}+{self.b}i'

    @ComplexOperation
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    @ComplexOperation
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    @ComplexOperation
    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    @ComplexOperation
    def __truediv__(self, other):
        div = other.a * other.a + other.b * other.b
        return Complex((self.a * other.a + self.b * other.b) / div,
                       (self.b * other.a - self.a * other.b) / div)


complex1 = Complex(1, 3)
complex2 = Complex(4, -5)
complex3 = complex1 + complex2
complex4 = complex1 - complex2
complex5 = complex1 * complex2
complex6 = complex1 / complex2
print(complex3)
print(complex4)
print(complex5)
print(complex6)

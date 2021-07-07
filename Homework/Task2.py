"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""


class Cloth:
    name = ""
    size = 0
    height = 0

    @property
    def cloth_needed(self):
        if isinstance(self, Coat):
            return self.size / 6.5 + 0.5
        elif isinstance(self, Costume):
            return self.height * 2 + 0.3
        else:
            raise TypeError("Не умею считать расход ткани для этой одежды")

    def __str__(self):
        return self.name


class Coat(Cloth):

    def __init__(self, size):
        self.size = size
        self.name = 'Пальто'


class Costume(Cloth):

    def __init__(self, height):
        self.height = height
        self.name = "Костюм"


if __name__ == "__main__":
    coat = Coat(32)
    costume = Costume(1.72)
    print(f"Для пошива {coat} нужно {coat.cloth_needed:.02f}m ткани")
    print(f"Для пошива {costume} нужно {costume.cloth_needed:.02f}m ткани")

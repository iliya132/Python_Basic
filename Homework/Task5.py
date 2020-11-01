"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра."""


class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self):
        self.title = "Pen"

    def draw(self):
        print("Вырисовывается ручка")


class Pencil(Stationery):

    def __init__(self):
        self.title = "Pencil"

    def draw(self):
        print("Вырисовывается карандаш")


class Handle(Stationery):

    def __init__(self):
        self.title = "Handle"

    def draw(self):
        print("Вырисовывается маркер")


stapler = Stationery()
stapler.title = "Stapler"
stapler.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()

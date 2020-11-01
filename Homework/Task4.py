"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
(WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    speed = 0
    color = "white"
    name = ""
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"машина {self.name} поехала вперед")

    def stop(self):
        print(f"машина {self.name} остановилась")

    def turn(self, direction):
        print(f"машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Зафиксировано превышение скорости на {self.speed - 60}")
        super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Зафиксировано превышение скорости на {self.speed - 40}")
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(65, "black", "chevrolet Aveo")
work_car = WorkCar(30, "yellow", "Cat")
sport_car = SportCar(320, "Red", "Bolid")
police_car = PoliceCar(110, "blue", "Chevrolet Camaro")
cars = [town_car, work_car, sport_car, police_car]

for car in cars:
    print(f"Диагностика автомобиля {car.name}")
    car.go()
    car.turn("налево")
    car.turn("направо")
    car.show_speed()
    car.stop()
    print(f"Цвет: {car.color}")
    print(f"Полицейский автомобиль: {car.is_police}")
    print()

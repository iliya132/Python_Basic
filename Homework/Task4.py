"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class OfficeAppliance:
    __id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = OfficeAppliance.__id
        OfficeAppliance.__id += 1


class Storage:
    __technic_list = []


class Printer(OfficeAppliance):
    def __init__(self, ppm: int):
        super().__init__(f"Printer_{self.id}")
        self.print_per_minute = ppm


class Scanner(OfficeAppliance):
    def __init__(self, scan_per_minute: int):
        super().__init__(f"Scanner_{self.id}")
        self.scan_per_minute = scan_per_minute


class Xerox(OfficeAppliance):
    def __init__(self, power_efficiency: str):
        super().__init__(f"Xerox{self.id}")
        self.power_efficiency = power_efficiency

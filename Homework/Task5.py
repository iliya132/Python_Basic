"""5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь."""


class ApplianceNotFound(Exception):
    def __init__(self, text = 'Appliance not found'):
        self.text = text


def ApplianceOperation(func):
    """Декоратор для Storage"""
    def Wrapper(self, appliance: OfficeAppliance, *args):
        if not isinstance(appliance, OfficeAppliance):
            raise ValueError("Функция работает только с типом OfficeAppliance")
        else:
            return func(self, appliance, *args)
    return Wrapper


class OfficeAppliance:
    __id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = OfficeAppliance.__id
        OfficeAppliance.__id += 1

    def __str__(self):
        return f'{self.name}_{self.id}'


class Storage:
    def __init__(self):
        self._all_technic_list = {}
        self._unit_technic_list = {}

    @ApplianceOperation
    def add_to_storage(self, appliance: OfficeAppliance):
        if type(appliance) in self._all_technic_list:
            self._all_technic_list[type(appliance)].append(appliance)
        else:
            self._all_technic_list.update({type(appliance): [appliance]})

    @ApplianceOperation
    def remove_from_storage(self, appliance: OfficeAppliance):
        if type(appliance) in self._all_technic_list:
            self._all_technic_list[type(appliance)].remove(appliance)

    @ApplianceOperation
    def any(self, appliance: OfficeAppliance):
        if type(appliance) in self._all_technic_list:
            container = self._all_technic_list[type(appliance)]
            if appliance in container:
                return True
            else:
                return False
        else:
            return False

    def get_by_id(self, id: int):
        for appliances in self._all_technic_list:
            for appliance in self._all_technic_list[appliances]:
                if appliance.id == id:
                    return appliance
        raise ApplianceNotFound()

    @ApplianceOperation
    def move_to_unit(self, appliance: OfficeAppliance, unit_name: str):
        if unit_name in self._unit_technic_list:
            if type(appliance) in self._unit_technic_list[str]:
                self._unit_technic_list[str].append(appliance)
            else:
                self._unit_technic_list[str].update({type(appliance): [appliance]})
        else:
            self._unit_technic_list.update({unit_name: {type(appliance): [appliance]}})

    @ApplianceOperation
    def get_unit(self, appliance):
        for unit in self._unit_technic_list:
            if type(appliance) in self._unit_technic_list[unit]:
                for appliance_type in self._unit_technic_list[unit]:
                    for item in self._unit_technic_list[unit][appliance_type]:
                        if item == appliance:
                            return unit
        return None


class Printer(OfficeAppliance):
    def __init__(self, ppm: int):
        super().__init__(f"Printer")
        self.print_per_minute = ppm


class Scanner(OfficeAppliance):
    def __init__(self, scan_per_minute: int):
        super().__init__(f"Scanner")
        self.scan_per_minute = scan_per_minute


class Xerox(OfficeAppliance):
    def __init__(self, power_efficiency: str):
        super().__init__(f"Xerox")
        self.power_efficiency = power_efficiency


if __name__ == "__main__":
    printer1 = Printer(20)
    xerox1 = Xerox("A+")
    scanner1 = Scanner(10)
    storage = Storage()
    storage.add_to_storage(printer1)
    storage.add_to_storage(xerox1)
    assert str(storage.get_by_id(2)) == "Xerox_2"
    assert str(storage.get_by_id(1)) == "Printer_1"
    assert not storage.any(scanner1)
    assert storage.any(printer1)
    assert storage.any(xerox1)
    storage.move_to_unit(xerox1, "Management")
    assert storage.get_unit(xerox1) == "Management"
    assert storage.get_unit(printer1) is None



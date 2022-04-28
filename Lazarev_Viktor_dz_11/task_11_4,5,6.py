class Warehouse:
    data_off_eq = {}
    count_equipment = 0

    def add_eq(self, equipment):
        """Заполнение склада"""

        if equipment._name in self.data_off_eq:
            self.data_off_eq[equipment._name].append(equipment)
        else:
            self.data_off_eq.setdefault(equipment._name, []).append(equipment)

    def search_equipment(self, name, brand):
        """Поиск техники по наименованию и марке"""

        if name in self.data_off_eq:
            for value in self.data_off_eq[name]:
                if brand in value.brand:
                    self.count_equipment += 1
                    print(value)
                else:
                    print(f'{name} марки {brand} на складе нет')
                    break
            print(f'\nОбщее количество {name}: {self.count_equipment}')
        else:
            print(f'{name} на складе нет')

    def show_all(self):
        """Показ всего товара на складе"""

        for key in self.data_off_eq:
            self.count_equipment += 1
            for data in self.data_off_eq[key]:
                self.count_equipment += 1
                print(data)
        print(f'всего товара {self.count_equipment}')


class OfficeEquipment:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


class Printer(OfficeEquipment):
    _name = 'Принтер'

    def __init__(self, brand, price, print_type):
        super().__init__(brand, price)
        self.print_type = print_type

    def __str__(self):
        return f'Принтер {self.brand}, цена {self.price}, тип песати {self.print_type}'


class Scaner(OfficeEquipment):
    _name = 'Сканер'

    def __init__(self, brand, price, scan_speed):
        super().__init__(brand, price)
        self.scan_speed = scan_speed

    def __str__(self):
        return f'Сканер {self.brand}, цена {self.price}, скорость сканирования {self.scan_speed}'


class Xerox(OfficeEquipment):
    _name = 'Ксерокс'

    def __init__(self, brand, price, paper_type):
        super().__init__(brand, price,)
        self.paper_type = paper_type
        self.count_equipment = 0

    def __str__(self):
        return f'Ксерокс {self.brand}, цена {self.price}, тип бумаги {self.paper_type}'


warehouse = Warehouse()


def warehouse_loading():
    """
    В функцию положил код чтоб можно было воспользоваться обработкой исключения с вызовом этой же функции
    :return: None
    """
    try:  #Если ввели не int число то ловим исключение и запускаем код вновь
        while True:  # Запрашиваю нужные параметры, и заполняю склад, до тех пор пока пользователь не загрузит всю технику
            equipment_1 = input('Что загружаем на склад Принтер, Сканер, Ксерокс? ').lower()
            brand_1 = input('Марка: ')
            price_1 = int(input('Цена: '))  #Проверку на валидность цены обернул в int и ловлю исключения для корректной работы
            add_parameter = input('Доп. параметр: ')
            if equipment_1 == 'принтер':
                warehouse.add_eq(Printer(brand_1, price_1, add_parameter))
            elif equipment_1 == 'сканер':
                warehouse.add_eq(Scaner(brand_1, price_1, add_parameter))
            else:
                warehouse.add_eq(Xerox(brand_1, price_1, add_parameter))
            more = input('Добавить технику Y чтобы выйти-нажмите любую другую клавишу? ').upper()
            if more != 'Y':
                break
    except ValueError:
        print('В поле цена должно быть число попробуйте снова')
        warehouse_loading()


def warehouse_search():
    """
    В функцию положил код чтоб можно было воспользоваться обработкой исключения с вызовом этой же функции
    :return: None
    """
    try:
        while True:  # Цикл для поиска определённой орг техники на складе, также можно запросить весь товар на складе
            equipment_2 = input('что ищем на складе? ').title()
            brand_2 = input('Марка: ')
            warehouse.search_equipment(equipment_2, brand_2)
            more = input('Искать ещё-Y, чтобы посмотреть весь товар-A,'
                         ' чтобы выйти-нажмите любую другую клавишу ').upper()
            if more == 'Y':
                continue
            elif more == 'A':
                warehouse.show_all()
            else:
                break
    except ValueError:
        print('В поле цена должно быть число попробуйте снова')
        warehouse_search()


warehouse_loading()
warehouse_search()

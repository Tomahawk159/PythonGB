class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(income)


class Position(Worker):
    def get_full_name(self):
        print(f'Работник: {self.surname} {self.name} \n'
              f'Должность: {self.position}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print('Полный доход составляет: ', total_income)


worker = Position('Иван', 'Иванов', 'механик', {'wage': 10000, 'bonus': 20000})
worker.get_full_name()
worker.get_total_income()

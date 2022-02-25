# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?


list_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for element in list_employees:
    employee_info = element.split()
    name_employee = employee_info[len(employee_info) - 1]
    correct_name = name_employee.capitalize()
    print(f'Привет {correct_name}')

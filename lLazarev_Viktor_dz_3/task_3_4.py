# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
# возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
# предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }


def thesaurus_adv(*args):
    peoples = {}
    for item in args:
        first_name, last_name = item.split()
        if last_name[0] in peoples.keys():
            if first_name[0] in peoples[last_name[0]].keys():
                peoples[last_name[0]][first_name[0]].append(item)
            else:
                peoples[last_name[0]].update({first_name[0]: [item]})
        else:
            peoples[last_name[0]] = {first_name[0]: [item]}
    return peoples


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)

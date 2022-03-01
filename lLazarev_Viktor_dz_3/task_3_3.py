# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }


def thesaurus(*args):
    names = {}
    for i in args:
        first_letter = i[0]
        if first_letter in names:
            names[first_letter].append(i)
        else:
            names[first_letter] = list(i.split())
    return names


result = thesaurus('Иван', 'Мария', 'Петр', 'Илья')
print(result)

from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Пётр', 'Сергей', 'Дмитрий',
          'Борис', 'Елена', 'Андрей', 'Анна']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А',
           '10Б', '9А']

tuple_gen = (tutor_class for tutor_class in zip_longest(tutors, classes, fillvalue=None)
             if not tutor_class[0] is None)

print(type(tuple_gen))
print(*tuple_gen)

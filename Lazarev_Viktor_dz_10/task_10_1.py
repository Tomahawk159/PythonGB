class Matrix:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def __str__(self):
        symbols = ''
        for numbers in self.numbers_list:
            for number in numbers:
                symbols += str(number) + ' '
            symbols += '\n'
        return symbols

    def __add__(self, other):
        sum_matrix = ''
        if len(self.numbers_list) != len(other.numbers_list):
            return f'Матрицы должны быть одинковы по количеству елементов'
        for lst_1, lst_2 in zip(self.numbers_list, other.numbers_list):
            if len(lst_1) != len(lst_2):
                return f'Матрицы должны быть одинковы по количеству елементов'
            for elem_1, elem_2 in zip(lst_1, lst_2):
                sum_matrix += str(elem_1 + elem_2) + ' '
            sum_matrix += '\n'
        return sum_matrix


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

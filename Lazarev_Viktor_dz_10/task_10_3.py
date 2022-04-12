class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __str__(self):
        return f'Количество яйчеек клетки {self.number_of_cells}'

    def __add__(self, other):
        return f'Объеденение клеток: {self.number_of_cells + other.number_of_cells}'

    def __sub__(self, other):
        result = self.number_of_cells - other.number_of_cells
        if result < 0:
            return f'Действие невозможно, результат меньше нуля'
        else:
            return f'Вычетание клеток: {result}'

    def __mul__(self, other):
        return f'Умножение клеток: {self.number_of_cells * other.number_of_cells}'

    def __truediv__(self, other):
        return f'Деление клеток:{round(self.number_of_cells / other.number_of_cells)}'

    def make_order(self, value):
        row = ''
        while self.number_of_cells > 0:
            if self.number_of_cells >= value:
                row += '*' * value + '\n'
            else:
                row += '*' * self.number_of_cells
            self.number_of_cells -= value
        return row


cell_1 = Cell(13)
cell_2 = Cell(11)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(4))

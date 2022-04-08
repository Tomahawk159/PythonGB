class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self, thickness):  #добавил параметр для толщины полотна в см.
        total_weight = (self._length * self._width * 25 * thickness) / 1000  #Разделил на 1000, перевёл в тонны
        print(f'Масса асфальта равна: {total_weight} тонн')


calculate_asphalt = Road(20, 5000)
calculate_asphalt.calculate_weight(5)

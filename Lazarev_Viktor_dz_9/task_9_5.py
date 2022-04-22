class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(f'{self.title} пишет')


class Pencil(Stationary):
    def draw(self):
        print(f'{self.title} чертит')


class Handle(Stationary):
    def draw(self):
        print(f'{self.title} рисует')


pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()

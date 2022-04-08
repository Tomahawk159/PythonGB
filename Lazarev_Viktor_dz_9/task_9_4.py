class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км\ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км\ч')
        if self.speed > 60:
            print(f'Превышение скорости, максимальная {60} км\ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км\ч')
        if self.speed > 40:
            print(f'Превышение скорости, максимальная {40} км\ч')


class PoliceCar(Car):
    pass


town_car = TownCar(100, 'чёрная', 'mazda', False)
town_car.go()
town_car.turn('Направо')
town_car.show_speed()
town_car.stop()

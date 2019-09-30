#  задание 1.1


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def car_move(self):
        print('Машина {} начала движение!'.format(self.name))

    def car_stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def car_turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police


my_car = Car(110, 'Silver', 'Chevrolet Cruze')

my_car.car_move()
my_car.car_turn('Направо')
my_car.car_stop()

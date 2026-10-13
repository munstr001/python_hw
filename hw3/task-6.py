class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def description(self):
        return f'{self.name}, скорость: {self.speed} км/ч'


class Car(Vehicle):
    def __init__(self, name, speed, seats):
        super().__init__(name, speed)
        self.seats = seats

    def description(self):
        return f'Автомобиль {super().description()}, мест: {self.seats}'


class Bicycle(Vehicle):
    def __init__(self, name, speed, gears):
        super().__init__(name, speed)
        self.gears = gears

    def description(self):
        return f'Велосипед {super().description()}, передач: {self.gears}'


class Boat(Vehicle):
    def __init__(self, name, speed, length):
        super().__init__(name, speed)
        self.length = length

    def description(self):
        return f'Катер {super().description()}, длина: {self.length} м'


if __name__ == '__main__':
    vehicles = [Car('Лада', 160, 5), Bicycle('Stels', 30, 7), Boat('Волна', 50, 6)]
    for vehicle in vehicles:
        print(vehicle.description())

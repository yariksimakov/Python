class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go - pedal to the floor {} {}'.format(self.name, self.color))

    def stop(self):
        print(f'stop {self.name, self.color}')

    def turn(self, direction = None):
        print(f'turn on {direction}')

    def show_speed(self):
        print(f'Speed you car {self.speed} km/h')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'You speed > 60 and = {self.speed} km/h')
        else:
            super().show_speed()

class SpotCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'You speed > 40 and = {self.speed} km/h')
        else:
            super().show_speed()

class PoliceCar(Car):
    pass


# run = Car(100, 'red', 'Mazda', False)
# run.go(), run.turn('left'), run.show_speed()


my_car = TownCar(200, 'red and blue', 'BMW', False)
my_car.go()
my_car.turn()
my_car.show_speed()
my_car.stop()

my_car_2 = WorkCar(100, 'yellow', 'Mazda', False)
my_car_2.go()
my_car.turn('straight')
my_car_2.show_speed()
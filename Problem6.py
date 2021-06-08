class Car:
    # , make, model, year, odometer, fuel
    def init(self):
        self.make = ''
        self.model = ''
        self.year = ''
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, distance):
        self.odometer += distance

    def __subtract_fuel(self, distance):
        self.fuel -= distance / 10

    def drive(self, distance):
        if self.fuel * 10 >= distance:
            print("Let’s drive!")
            self.__add_distance(distance)
            self.__subtract_fuel(distance)
        else:
            print("Need more fuel, please, fill more!")


BMW = Car()
BMW.drive(1000)
BMW.drive(696)
BMW.drive(10)
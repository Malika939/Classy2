class Person:
    def walk(self):
        print(' Идти')

class Driver(Person):
    def drive_car(self):
        print('Водить машину')

 class Cooker(Driver):

   p = Person()
p.walk()
d = Driver()
d.drive_car()

c = Cooker()
c.drive_car()
class Airplane:
    def __init__(self, model, year, max_speed, odometer=0, is_flying=False):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0

    def take_off(self):
        self.is_flying = True
        print(f'somolet {self.model}, vzletel so skorostiy {self.max_speed}, rasstoyanie {self.odometer}')

    def fly(self):
            self.odometer += 100 
        
    def land(self):
        self.is_flying = False


a = Airplane(model="Boing", year="1990", max_speed="100")
a.fly()
a.take_off()
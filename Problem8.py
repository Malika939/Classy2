class Soldier():
    def __init__(self, name, guns):
        self.name = name
        self.guns = guns

class Guns():
    def shoots(self):
        print(f'{self.name} стрелял с {self.guns}')
        self.shop = 30
        while self.shop > 0:
            self.shop -= 1
            print(self.shop)
            if self.shop == 0:
                print("нужно перезаридится")
                self.strelka()
            else:
                pass

    def strelka(self):
        self.strelok = input('prodolzhit strelbu? y/n:') 
        if self.strelok == 'y':
            self.shoots()
        else:
            pass

class Act_of_Shooting(Soldier, Guns):
    def init(self, name, guns):
        Soldier.init(self, name, guns)
        
s = Act_of_Shooting("Myrza", "Ak_47")
s.shoots()
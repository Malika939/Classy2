class Factory:
    def engine(self):
        print('Двигатель создан')
    def bridge(self):
        print('Ходовая часть создана')


class Toyota(Factory):
    def wheels(self):
        print('Колёса готовы')
    def windows(self):
        print('Стёкла готовы') 


t = Toyota()          
t.wheels()
f = Factory()
f.engine()  

l = []
l.append(t.bridge())
l.append(t.engine())
l.append(t.wheels())
l.append(t.windows())
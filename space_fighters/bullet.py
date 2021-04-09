# coding=utf8

class Bullet1(object):                 # Пуля (тех-объект)
    def __init__(self):
        self.x = 0
        self.y = 0
        self.spawned = False
        self.col = color(0)
        self.vX = 0
    def shoot(self,xCord,yCord,var, spd = 0):      # Создание пуль
        self.x = xCord
        self.y = yCord
        self.spawned = True
        self.col = var
        self.vX = spd
    def created(self):               # Запрос: существует ли пуля?
        return(self.spawned)
    def posX(self):               # Запрос координаты по ИКСУ
        return(self.x)
    def posY(self):               # Запрос координаты по ИГРЕКУ
        return(self.y)
    def fly(self, spd, ary):                # Полёт пули
        self.y -= spd
        self.x -= self.vX
        noStroke()
        fill(self.col)
        ellipse(self.x,self.y,10,10)
        if self.y <= -30:
            ary.pop(ary.index(self))
        if self.y >= height + 30:
            ary.pop(ary.index(self))

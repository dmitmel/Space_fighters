# coding=utf8

import bullet

class Enemy1(object):                   # Враги (тех-объект)
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ani = True
        self.health = 100
        self.spawned = False
        self.inDex = 0
        self.CBD = False
        self.DBA = 20
        self.DBS = 0
        self.HBV = self.health
        self.shield = 0
    def spawn(self,xCord,yCord):    # Создание врагов
        self.x = xCord
        self.y = yCord
        self.spawned = True
    def created(self):            # Запрос: существует ли пуля?
        return(self.spawned)
    def move(self,yCord,spd):           # Вылет на боевую позицию
        if self.y < yCord:
            self.y += spd
        if self.y == yCord:
            self.CBD = True
    def show(self, img1, img2):                  # Показываем (в виде картинки) врага
        if self.ani:
            image(img1, self.x, self.y)
        else:
            image(img2, self.x, self.y)
        if frameCount % 20 == 0:
            self.ani = not(self.ani)
    def posX(self):               # Запрос координаты по ИКСУ
        return(self.x)
    def posY(self):               # Запрос координаты по ИГРЕКУ
        return(self.y)
    def damage(self, dmg):        # Нанисение урона
        if self.CBD:
            self.health -= dmg
            self.shield = 20
    def getHealth(self):          # Запрос жизней
        return(self.health)
    def showHealth(self):         # Поазываем примоугольник с жызнями
        noStroke()
        fill('#E82D0C')
        rectMode(CENTER)
        if self.health < 100:
            rect(self.x, self.y - 80, self.HBV, 10)
        if self.HBV > self.health:
            self.HBV -= 0.5
        if self.HBV < self.health:
            self.HBV += 0.5
        if self.shield > 0:
            self.shield -= 1
            ellipseMode(CENTER)
            strokeWeight(self.shield / 3)
            stroke('#1A8E13')
            noFill()
            ellipse(self.x, self.y, 150, 150)
    def shoot(self, ary):              # Стрельба у врагов
        if self.DBS > 0:
            self.DBS -= 1
        if frameCount % self.DBA == 0 and self.DBS == 0:    
            if self.CBD:
                b = bullet.Bullet1()
                b.shoot(self.x,height - 520,'#00E01B', random(-1, 1))
                ary.append(b)
                self.DBA = int(random(40, 60))
                self.DBS = 20


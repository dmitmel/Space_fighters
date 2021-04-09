class Bullet1(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.spawned = False
        self.col = color(0)
        self.vX = 0
    def shoot(self,xCord,yCord,var, spd = 0):
        self.x = xCord
        self.y = yCord
        self.spawned = True
        self.col = var
        self.vX = spd
    def created(self):  
        return(self.spawned)
    def posX(self):   
        return(self.x)
    def posY(self):          
        return(self.y)
    def fly(self, spd, ary):          
        self.y -= spd
        self.x -= self.vX
        noStroke()
        fill(self.col)
        ellipse(self.x,self.y,10,10)
        if self.y <= -30:
            ary.pop(ary.index(self))
        if self.y >= height + 30:
            ary.pop(ary.index(self))
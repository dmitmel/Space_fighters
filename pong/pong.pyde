from time import sleep
r = 0
g = 0
b = 0
l = 0
colSpd = 12
lx = 101
wdth = 800
hght = 500
winner = '3'
gameState = 0
spd = 11
s1 = 0
s2 = 0
x = wdth / 2 - 10
y = hght / 2 - 10
ballVx = 11
if random(0,2) == 1:
    ballVx = -ballVx
ballVy = 2
pl1 = hght / 2
pl2 = hght / 2
menu = 'main'
score1 = 0
score2 = 0
cSpd = 0
click = False
auto = False
def setup():
    size(wdth,hght)
    background(0)
    stroke(255)
    fill(100)
    rect(100,300,600,30)
def reDraw():
    global x, y, pl1, pl2, score
    background(0)
    textSize(200)
    fill(203,25,25)
    text('PONG',110,320)
    fill(10,173,38)
    text('PON',110,320)
    fill(42,12,165)
    text('PO',110,320)
    fill(240,216,2)
    text('P',110,320)
    textSize(60)
    fill(80,3,108)
    text(str(score1) + ' : ' + str(score2),320,70)
    noStroke()
    fill(255)
    ellipse(x,y,20,20)
    fill(100)
    rect(0,0,10,500)
    rect(0,0,800,10)
    rect(790,0,800,500)
    rect(0,490,800,500)
    fill(206,8,8)
    rect(35,pl1,10,100)
    fill(20,147,4)
    rect(755,pl2,10,100)
def draw():
    global x, y, pl1, pl2, spd, ballVx, hght, wdth, ballVy, score1, score2, gameState, winner, s1, s2, score, menu, click, auto, cSpd, r, g, b, l, lx
    if gameState == 0:
        if int(random(0,2)) == 1:
            stroke(r,g,b)
            if l == 0:
                r = r + colSpd
            if l == 1:
                g = g + colSpd
            if l == 2:
                r = r - colSpd
                g = g + colSpd
            if l == 3:
                r = r - colSpd
                g = g + colSpd
            if l == 4:
                g = g - colSpd
                b = b + colSpd
            if l == 5:
                r = r + colSpd
                g = g + colSpd
            if r > 200:
                l = 1
            if r > 200 and g > 200:
                l = 2
            if g > 200:
                l = 3
            if g > 200 and r < 0:
                l = 4
            if b > 470:
                l = 5
            if r > 200 and g > 200 and b > 200:
                l = 6
            fill(r,g,b)
            rect(lx,301,5,28)
            textSize(50)
            text('LOADING',290,265)
            if lx < 705:
                lx = lx + 5
            if lx >= 705:
                sleep(1)
                gameState = 2
    if not(mousePressed):
        click = False
    if gameState == 1:
        reDraw()
        s1 = score1
        s2 = score2
        if not(auto):
            if keyPressed and key == 'w' and pl1 > 10:
                pl1 = pl1 - spd
            if keyPressed and key == 's' and pl1 < 390:
                pl1 = pl1 + spd
        else:
            cSpd = dist(35,pl1+50,35,y-10)
            if cSpd > 8:
                cSpd = 8
            if y < pl1+50 and pl1 > 10:
                pl1 = pl1 - cSpd
            elif y > pl1+50 and pl1 < 390:
                pl1 = pl1 + cSpd
        if keyPressed and keyCode == UP and pl2 > 10:
            pl2 = pl2 - spd
        if keyPressed and keyCode == DOWN and pl2 < 390:
            pl2 = pl2 + spd
    
        x = x + ballVx
        y = y + ballVy
    
        if x >= 740 and pl2 <= y and pl2 + 100 >= y and ballVx > 0:
            ballVx = -ballVx
        if x <= 60 and pl1 <= y and pl1 + 100 >= y and ballVx < 0:
            ballVx = -ballVx
        
        if y <= 20:
            ballVy = -ballVy
        if y >= 480:
            ballVy = -ballVy
        
        if x < -30:
            x = wdth / 2
            ballVx = -ballVx
            ballVy = 2
            y = hght / 2
            score2 = score2 + 1
        if x > 830:
            x = wdth / 2
            ballVx = -ballVx
            ballVy = 2
            y = hght / 2
            score1 = score1 + 1
    
        if score1 == 10 or score2 == 10:
            gameState = 2
            
        if score1 == 10:
            winner = '1'
        if score2 == 10:
            winner = '2'
        
        if keyPressed and keyCode == 16:
            x = wdth / 2 - 10
            y = hght / 2 - 10
            s1 = 0
            s2 = 0
            winner = '3'
            gameState = 2
        if not(auto) and keyPressed and key == 'q':
            x = wdth / 2 - 10
            y = hght / 2 - 10
            s1 = 0
            s2 = 0
            winner = '3'
            gameState = 2
        
        delay(7)
        
    if gameState == 2:
        reDraw()
        if random(0,2) == 1:
            ballVx = -ballVx
        fill(0)
        stroke(0)
        rect(300,11,200,60)
        fill(100)
        textSize(60)
        fill(80,3,108)
        if winner == '1':
            text('10 : '+str(s2),320,70)
            textSize(50)
            text('Winner!',80,60)
        if winner == '2':
            text(str(s1)+' : 10',320,70)
            textSize(50)
            text('Winner!',550,60)
        if winner == '3':
            text('0 : 0',320,70)
        textSize(40)
        if menu == 'main':
            if mouseX >= 580 and mouseY >= 416 and mouseX <= 774 and mouseY <= 473:
                fill(60,142,13)
            else:
                fill(100)
            text('RESTART',590,460)
            if mouseX >= 230 and mouseY >= 360 and mouseX <= 570 and mouseY <= 410:
                fill(255)
            else:
                fill(100)
            text('PLAY NEW GAME',240,400)
            if mouseX >= 260 and mouseY >= 420 and mouseX <= 530 and mouseY <= 470:
                fill(255)
            else:
                fill(100)
            text('USEFUL INFO',270,460)
            if mouseX >= 30 and mouseY >= 420 and mouseX <= 135 and mouseY <= 470:
                fill(206,8,8)
            else:
                fill(100)
            text('EXIT',40,460)
            if mouseX >= 230 and mouseY >= 360 and mouseX <= 570 and mouseY <= 410 and mousePressed and not(click):
                click = True
                menu = 'game'
            if mouseX >= 30 and mouseY >= 420 and mouseX <= 135 and mouseY <= 470 and mousePressed and not(click):
                click = True
                exit()
            if mouseX >= 580 and mouseY >= 416 and mouseX <= 774 and mouseY <= 473 and mousePressed and not(click):
                click = True
                gameState = 0
        elif menu == 'game':
            if mouseX >= 210 and mouseY >= 360 and mouseX <= 610 and mouseY <= 410:
                fill(255)
            else:
                fill(100)
            text('PLAYER VS PLAYER',220,400)
            if mouseX >= 175 and mouseY >= 420 and mouseX <= 627 and mouseY <= 470:
                fill(255)
            else:
                fill(100)
            text('PLAYER VS COMPUTER',185,460)
            if mouseX >= 30 and mouseY >= 420 and mouseX <= 153 and mouseY <= 470:
                fill(206,8,8)
            else:
                fill(100)
            text('BACK',40,460)
            if mouseX >= 175 and mouseY >= 420 and mouseX <= 627 and mouseY <= 470 and mousePressed and click == False:
                auto = True
                click = True
                gameState = 1
            if mouseX >= 210 and mouseY >= 360 and mouseX <= 610 and mouseY <= 410 and mousePressed and click == False:
                auto = False
                click = True
                gameState = 1
            if mouseX >= 30 and mouseY >= 420 and mouseX <= 153 and mouseY <= 470 and mousePressed and click == False:
                click = True
                menu = 'main'
        score1 = 0
        score2 = 0
        pl1 = hght / 2
        pl2 = hght / 2
    

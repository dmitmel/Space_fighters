import bullet, enemy

class Enemy(enemy.Enemy1):
    pass
            
class Bullet(bullet.Bullet1):
    pass

def setup():
    global highscore, white, x, y, spd, player, shipAni, maxSpeed, bullets, bulletColor, health, dmg, gunLvl, shootSpd, enemies, ship1, ship2, enemy1, enemy2, accseleration, ESP, movingL, movingR, shooting, bar, enemy_bullets, newGame, colors, DAD, gunType, state, score, SHB, HBN, click, expls

    main = loadStrings('main.txt')
    config = loadStrings('config.txt')
    
    size(int(loadStrings('config.txt')[0][8:]),int(loadStrings('config.txt')[1][8:]))
    ship1 = PImage
    ship2 = PImage
    enemy1 = loadImage('textures/objects/enemy_1.png')
    enemy2 = loadImage('textures/objects/enemy_2.png')
    bar = loadImage('textures/objects/health_bar.png')
    font = loadFont('AgencyFB-Reg-48.vlw')
    highscore = int(main[1][12:])
    newGame = main[0][13:] == 'True'
    print(newGame)
    if newGame:
        saveStrings('main.txt', ['first game = False','highscore = '+str(highscore)])
    loadShip(True)

    state = 1
    x = int(config[0][8:]) / 2
    dataFile = ''
    armour = 0
    gunLvl = 0
    accseleration = 0
    maxSpeed = 0
    colors = []
    name = ''
    gunType = ''
    
    loadShip(debug=True)
    
    spd = 0
    mode = 0
    shipAni = True
    bullets = []
    enemies = ["","","",""]
    bulletColor = True
    health = 100
    dmg = 2 + gunLvl
    shootSpd = 30 - gunLvl * 2
    ESP = 0
    movingL = False
    movingR = False
    shooting = False
    enemy_bullets = []
    DAD = 0
    textFont(font)
    score = 0
    SHB = False
    HBN = health
    y = height - 190
    click = False
    white = 0
        

def loadShip(debug = False, direct = 'ship_data/F-506'):
    global newGame, dataFile, armour, gunLvl, accseleration, maxSpeed, colors, dmg, shootSpd, gunType, ship1, ship2
    dataFile = loadStrings('ship_data/F-506/data.txt')
    ship1 = loadImage(direct + '/ship_1.png')
    ship2 = loadImage(direct + '/ship_2.png')
    if debug:
        for var in dataFile:
            print(var)
    armour = int(dataFile[0][7:])
    gunLvl = int(dataFile[1][11:])
    accseleration = float(dataFile[2][15:])
    maxSpeed = float(dataFile[3][11:])
    colors = []
    for i in range (5, 8):
        if dataFile[i][9:] != 'None':
            colors.append(dataFile[i][9:])
    name = dataFile[8][7:]
    gunType = dataFile[9][11:]
    if gunType == 'simple blaster':
        dmg = 2 + gunLvl
        shootSpd = 30 - gunLvl * 2
    if name == 'F-506':
        tier = 1
    
def in_box(x1, y1, x2, y2, tx, ty):
    if tx > x1 and ty > y1 and tx < x2 and ty < y2:
        return True
    else:
        return False
    
def draw():
    global highscore, white, x, y, spd, player, shipAni, maxSpeed, bullets, bulletColor, health, dmg, gunLvl, shootSpd, enemies, ship1, ship2, enemy1, enemy2, accseleration, ESP, movingL, movingR, shooting, bar, enemy_bullets, colors, DAD, gunType, state, score, SHB, HBN, click, expls
    if state == 1 or state == 2:
        if health < HBN:
            HBN -= 0.5
        if health > HBN:
            HBN += 0.5
            
        if score < 0:
            score = 0
        if shootSpd < 5:
            shootSpd = 5
        if gunType == 'simple blaster':
            dmg = 2 + gunLvl
            shootSpd = 30 - gunLvl * 2
        background(10)
        imageMode(CORNER)
        image(bar, 1, height - 88)
        noStroke()
        rectMode(CORNER)
        fill(map(HBN, 0, 100, 80, 220), 0, 0)
        rect(82, height - 67, 214.0 / 100.0 * float(HBN), 61)
        textAlign(RIGHT, TOP)
        fill(240)
        text('score: ' + str(int(score)), width - 10, 15)
        imageMode(CENTER)
        if health <= 0:
            health = 0
            state = 2
        else:
            y = height - 190
        
        if frameCount % 20 == 0:
            shipAni = not(shipAni)
        if shipAni:
            image(ship1, x, y)
        else:
            image(ship2, x, y)
        
        if spd > maxSpeed:
            spd = maxSpeed
        if spd < -maxSpeed:
            spd = -maxSpeed
        if not(keyPressed):
            movingL = False
            movingR = False
            shooting = False
            spd = 0
            click = False
        if ((key == 'a' and keyPressed) or movingL) and state == 1:
            score += 0.02
            spd += accseleration
            x -= spd
        if ((key == 'd' and keyPressed) or movingR) and state == 1:
            score += 0.02
            spd += accseleration
            x += spd
            
        if x <= -61:
            x = width + 60
        if x >= width + 61:
            x = -60
            
        if key == 'a' and keyPressed:
            movingL = True
        if key == 'd' and keyPressed:
            movingR = True
        if ((keyCode == ' ' and keyPressed) or shooting) and frameCount % shootSpd == 0 and state == 1:
            bullets.append(Bullet())
        if key == ' ' and keyPressed:
            shooting = True
             
        if keyPressed and keyCode == 112 and not(click):
            SHB = not(SHB)
            click = True
        
        
        if frameCount % shootSpd == 0:
            bulletColor = not(bulletColor) 
        for bullet in bullets:
            if not(bullet.created()):
                if bulletColor:
                    bullet.shoot(x - 30,height - 220, colors[0])
                else:
                    bullet.shoot(x + 30,height - 220, colors[1])

            bullet.fly(5 + gunLvl / 4, bullets)
            
        for bullet in enemy_bullets:
            if not(bullet.created()):
                bullet.shoot(x,height - 520,'#00E01B')
                
            bullet.fly(-5, enemy_bullets)
            if in_box(x - 50, y - 50, x + 50, y + 50, bullet.posX(), bullet.posY()) and state == 1:
                health -= 2
                enemy_bullets.pop(enemy_bullets.index(bullet))
                score -= 1
                DAD = 20
        
        if DAD > 0:
            DAD -= 1
            ellipseMode(CENTER)
            strokeWeight(DAD / 3)
            stroke(12, 186, 232)
            noFill()
            ellipse(x, y, 150, 150)
        
        for item in enemies:
                if type(item) != Enemy:
                    enemies[enemies.index(item)] = Enemy()
                    
        for item in enemies:
            if type(item) == Enemy:
                if not(item.created()) and ESP == 0:
                    item.spawn(width / 5 * (enemies.index(item) + 1), -200)
                    ESP = int(random(0,100))
                
                if item.created():
                    item.move(200,8)
                    item.show(enemy1, enemy2)
                    
            for bullet in bullets:
                
                if in_box(item.posX() - 57, item.posY() - 60, item.posX() + 57, item.posY() + 40, bullet.posX(), bullet.posY()):
                    bullets.pop(bullets.index(bullet))
                    item.damage(dmg)
                    score += 2
                    
                    if item.getHealth() <= 0:
                        enemies[enemies.index(item)] = ""
                        score += 20
                        
            item.showHealth()
            item.shoot(enemy_bullets)
            
            if SHB:
                rectMode(CORNERS)
                strokeWeight(7)
                noFill()
                stroke(200,0,0)
                rect(item.posX() - 57, item.posY() - 60, item.posX() + 57, item.posY() + 40)
                
        if SHB:
            rectMode(CORNERS)
            strokeWeight(7)
            noFill()
            stroke(200,0,0)
            rect(x - 50, y - 50, x + 50, y + 50)
        if ESP > 0:
            ESP -= 1
            
        if state == 2:
            if score > highscore:
                saveStrings('main.txt', ['first game = False','highscore = '+str(int(score))])
        
    if keyPressed and keyCode == 113 and not(click):
        saveFrame('screenshots/space_fighters '+str(millis())+'.'+str(second())+'.'+str(day())+'.'+str(month())+'.\
 .'+str(year())+'.png')
        white = 255
        click = True
    if white > 200:
        background(white)
        white -= 5
    if white < 200:
        white = 200
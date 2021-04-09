# Импортим нужные библиотеки

import bullet, enemy

# Добавляем нужные методы классам

class Enemy(enemy.Enemy1):
    pass
            
class Bullet(bullet.Bullet1):
    pass

def setup():
    global highscore, white, x, y, spd, player, shipAni, maxSpeed, bullets, bulletColor, health, dmg, gunLvl, shootSpd, enemies, ship1, ship2, enemy1, enemy2, accseleration, ESP, movingL, movingR, shooting, bar, enemy_bullets, newGame, colors, DAD, gunType, state, score, SHB, HBN, click, expls
    
    # ================================== Загрузка файлов из директории игры ========================================
    
    main = loadStrings('main.txt')
    config = loadStrings('config.txt')
    
    size(int(loadStrings('config.txt')[0][8:]),int(loadStrings('config.txt')[1][8:]))        # Создание графического окна (по настройкам файла config)
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
    
    # ================================== Объвление нужных переменных =================================================
    
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
            
        

def loadShip(debug = False, direct = 'ship_data/F-506'):                             # Загрузка данных коробля
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
    
def in_box(x1, y1, x2, y2, tx, ty):                      # Функция для проверки Hit-box'а
    if tx > x1 and ty > y1 and tx < x2 and ty < y2:
        return True
    else:
        return False
    
def draw():
    global highscore, white, x, y, spd, player, shipAni, maxSpeed, bullets, bulletColor, health, dmg, gunLvl, shootSpd, enemies, ship1, ship2, enemy1, enemy2, accseleration, ESP, movingL, movingR, shooting, bar, enemy_bullets, colors, DAD, gunType, state, score, SHB, HBN, click, expls
    if state == 1 or state == 2:                         # Работа игры
        if health < HBN:                    # Анимация health-bar'а
            HBN -= 0.5
        if health > HBN:
            HBN += 0.5
            
        if score < 0:                     # Ограничитель счётчика очков
            score = 0
        if shootSpd < 5:                  # Макс. скорость
            shootSpd = 5
        if gunType == 'simple blaster':   # Тип оружия
            dmg = 2 + gunLvl
            shootSpd = 30 - gunLvl * 2
        background(10)                    # Небольшая часть графики
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
        if health <= 0:                   # Ограничитель жизней
            health = 0
            state = 2
        else:
            y = height - 190
        # ======================================== Анимация и движение корабля ========================================
        if frameCount % 20 == 0:      # "анимация" корабля
            shipAni = not(shipAni)
        if shipAni:
            image(ship1, x, y)
        else:
            image(ship2, x, y)
        
        if spd > maxSpeed:         # Ограничитель скорости
            spd = maxSpeed
        if spd < -maxSpeed:
            spd = -maxSpeed
        if not(keyPressed):        # Управление
            movingL = False
            movingR = False
            shooting = False
            spd = 0
            click = False
        if ((key == 'a' and keyPressed) or movingL) and state == 1:    # Движение влево
            score += 0.02
            spd += accseleration
            x -= spd
        if ((key == 'd' and keyPressed) or movingR) and state == 1:    # Движение вправо
            score += 0.02
            spd += accseleration
            x += spd
            
        if x <= -61:                  # Телепортация при выходе за границу
            x = width + 60
        if x >= width + 61:
            x = -60
            
        if key == 'a' and keyPressed:
            movingL = True
        if key == 'd' and keyPressed:
            movingR = True
        if ((keyCode == ' ' and keyPressed) or shooting) and frameCount % shootSpd == 0 and state == 1:    # Стрельба
            bullets.append(Bullet())
        if key == ' ' and keyPressed:
            shooting = True
             
        if keyPressed and keyCode == 112 and not(click):    # Показ hit-box'а
            SHB = not(SHB)
            click = True
            
        # --------------------------------------------------------------------------
        
        if frameCount % shootSpd == 0:
            bulletColor = not(bulletColor) 
        for bullet in bullets:            # Проверка каждой пули
            if not(bullet.created()):     # Если пули ещё нету, надо её создать
                if bulletColor:
                    bullet.shoot(x - 30,height - 220, colors[0])
                else:
                    bullet.shoot(x + 30,height - 220, colors[1])
                                        # Просчёт полёта
            bullet.fly(5 + gunLvl / 4, bullets)
            
        for bullet in enemy_bullets:            # Проверка каждой пули (вражеской)
            if not(bullet.created()):     # Если пули ещё нету, надо её создать
                bullet.shoot(x,height - 520,'#00E01B')
                                        # Просчёт полёта
            bullet.fly(-5, enemy_bullets)
            if in_box(x - 50, y - 50, x + 50, y + 50, bullet.posX(), bullet.posY()) and state == 1:   # Что делать, если в корабль попадает пуля
                health -= 2
                enemy_bullets.pop(enemy_bullets.index(bullet))
                score -= 1
                DAD = 20
        
        if DAD > 0:     # Красивый ефект шита (у твоего корабля)
            DAD -= 1
            ellipseMode(CENTER)
            strokeWeight(DAD / 3)
            stroke(12, 186, 232)
            noFill()
            ellipse(x, y, 150, 150)
            
        # ============================== Код врагов ====================================
        for item in enemies:                           # Создание врагов
                if type(item) != Enemy:
                    enemies[enemies.index(item)] = Enemy()
                    
        for item in enemies:                       # Просчёт врагов
            if type(item) == Enemy:                # Если существует враг...
                if not(item.created()) and ESP == 0:    # Спавн врагов
                    item.spawn(width / 5 * (enemies.index(item) + 1), -200)
                    ESP = int(random(0,100))
                
                if item.created():                # Анимация
                    item.move(200,8)
                    item.show(enemy1, enemy2)
                    
            for bullet in bullets:               # Обработка с участием пуль
                
                if in_box(item.posX() - 57, item.posY() - 60, item.posX() + 57, item.posY() + 40, bullet.posX(), bullet.posY()):     # Если пуля попала...
                    bullets.pop(bullets.index(bullet))
                    item.damage(dmg)
                    score += 2
                    
                    if item.getHealth() <= 0:                     # ...А может быть уничтожила врага...
                        enemies[enemies.index(item)] = ""
                        score += 20
                        
            item.showHealth()             # Функции, которые делают врагов менее статичными
            item.shoot(enemy_bullets)
            
            if SHB:                 # Показ hit-box'а (у врагов)
                rectMode(CORNERS)
                strokeWeight(7)
                noFill()
                stroke(200,0,0)
                rect(item.posX() - 57, item.posY() - 60, item.posX() + 57, item.posY() + 40)
                
        if SHB:                 # Показ hit-box'а (у корабля)
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
        
    if keyPressed and keyCode == 113 and not(click):           # Создание screenshot'а
        saveFrame('screenshots/space_fighters '+str(millis())+'.'+str(second())+'.'+str(day())+'.'+str(month())+'.\
  '+str(year())+'.png')
        white = 255
        click = True
    if white > 200:
        background(white)
        white -= 5
    if white < 200:
        white = 200

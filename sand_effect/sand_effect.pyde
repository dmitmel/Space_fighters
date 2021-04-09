# ЛУЧШЕ ЭТО ПРОЧИТАТЬ!!!
# Инструкция по использованию этой программы:
# 1) Вставить в Processing
# 2) Запустить
# 3) Кликнуть где-угодно в открытом окне
# 4) ОФИГЕТЬ (не обязательный пункт)

# Массивы, которые позже станут 2D'шными, для хранения данных о каждой клетке:
grid = []         # Сетка
DBFs = []         # Задержка между сдвигом вниз
clicks = []       # Клики

s1 = 20                  # Размеры сетки
s2 = s1 * (50 / s1)

barier = True            # Переменная для хранения состояния барьера

brush_size = 1           # Размер кисти

# Все простые цвета
white_col = 255    # Белый
black_col = 0      # Чёрный
red_col = '#ED0A0A'         # Каждый (красный)
orange_col = '#FCA117'      # Охотник (оранжевый)
yellow_col = '#F7DC0A'      # Желает (жёлтый)
green_col = '#34B200'       # Знать (зелёный)
light_blue_col = '#21A4E8'  # Где (голубой)
blue_col = '#0500B2'        # Сидит (синий)
purple_col = '#C617FC'      # Фазан (фиолетовый)

sand_col = red_col          # Цвет песочка
barier_col1 = yellow_col    # Цвет1 барьера
barier_col2 = black_col     # Цвет2 барьера

for x in range(s1):     # Конструктор 2D массивов
    grid.append([])
    DBFs.append([])
    clicks.append([])
    for y in range(s1 + 1):
        grid[x].append(white_col)
        DBFs[x].append(0)
        clicks[x].append(False)
        
def setup():                # Тут, я думаю всё понятно
    global s1, s2
    size(s2 * s1 + 1, s2 * s1 + 1)
    
def draw():
    global s1, s2, clicks, DBFs, barier, brush_size, barier_col1, barier_col2, sand_col, black_col, white_col, red_col, orange_col, yellow_col, green_col, light_blue_col, blue_col, purple_col
    for x in range(s1):         # Пробег по всем клеткам
        for y in range(s1):
            
            if not(mousePressed): clicks[x][y] = False     # Система клика (есть продлжение)
            
            fill(grid[x][y])                               # Графика (Прорисовка, а не анимация)
            if grid[x][y] == white_col: stroke(0)
            else: stroke(white_col)
            rect(x * s2, y * s2, s2, s2)
            
            if mouseX > x * s2 and mouseY > y * s2 and mouseX < x * s2 + s2 and mouseY < y * s2 + s2:     # Рисование песка + система клика
                if mouseButton == LEFT and mousePressed and not(clicks[x][y]):
                    grid[x][y] = sand_col
                    DBFs[x][y] = 8
                    
                    if brush_size > 1:
                        
                        for i in range(1, brush_size):    # Часть, которая отвечает за размер кисти (недоработаная)
                            if x + i < s1: grid[x + i][y] = sand_col
                            if y + i < s1: grid[x][y + i] = sand_col
                            if x - i > -1: grid[x - i][y] = sand_col
                            if y - i > -1: grid[x][y - i] = sand_col
                            
                    clicks[x][y] = True
                    
                if mouseButton == RIGHT and mousePressed and not(clicks[x][y]):       # Вкл./Выкл. барьера
                    barier = not(barier)
                    clicks[x][y] = True
            else:
                clicks[x][y] = False
            
            if y + 1 < s1 and DBFs[x][y] == 0 and grid[x][y] != white_col:          # Анимация падения:
                if y + 1 < s1 and grid[x][y + 1] == white_col:                      # Если можно упасть вниз - падаем вниз
                    grid[x][y] = white_col
                    grid[x][y + 1] = sand_col
                    DBFs[x][y + 1] = 8
                elif grid[x][y + 1] != white_col and x + 1 < s1 and x - 1 > -1:     # Иначе:
                    
                    var = int(random(1, 3))                                          # Выбор направления
                    
                    if grid[x + 1][y] == white_col and grid[x + 1][y + 1] == white_col and DBFs[x + 1][y + 1] == 0 and var == 1:     # Падение вправо
                        grid[x][y] = white_col
                        grid[x + 1][y] = sand_col
                        
                    if grid[x - 1][y] == white_col and grid[x - 1][y + 1] == white_col and DBFs[x - 1][y + 1] == 0 and var == 2:     # Падение влево
                        grid[x][y] = white_col
                        grid[x - 1][y] = sand_col
                    
            if y + 1 == s1 and DBFs[x][y] == 0:       # Удаление при выпадании под низ
                grid[x][y] = white_col
                
            if y < s1 - 1 and DBFs[x][y + 1] > 0: DBFs[x][y + 1] -= 1                          # Задержка между сдвигами вниз
            if y == 0 and DBFs[x][0] > 0: DBFs[x][0] -= 1                                      # Задержка между сдвигами вниз (специально для самой верхней строки)
            
            if barier:                 # Показ барьера
                if y == s1 - 1:
                    if x % 2 == 0: grid[x][y] = barier_col1
                    else: grid[x][y] = barier_col2
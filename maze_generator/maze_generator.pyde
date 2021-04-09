# Массивы, которые позже станут 2D'шными, для хранения данных о каждой клетке:
maze = []         # Лабиринт
DBCs = []

s1 = 71                  # Размеры сетки
s2 = 10

debounce_size = 15
state = 1

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

bot_col = green_col
wall_col = black_col
uv_unit_col = red_col
v_unit_col = white_col
uv_units = 0
debounce = 0
pFound = False
exit_var = False
d = 1

for x in range(s1):     # Конструктор 2D массивов
    maze.append([])
    DBCs.append([])
    for y in range(s1 + 1):
        if x % 2 != 0 and y % 2 != 0: maze[x].append(uv_unit_col)
        else: maze[x].append(wall_col)
        DBCs[x].append(0)
        if int(random(0, 10)) == 1: print('loading... co-ords - x: %i + y: %i' % (x, y))

center = int(s1 / 2) - 1
sX = 1
sY = 1

maze[sX][sY] = bot_col
bX = sX
bY = sY

for x in range(s1):         # Пробег по всем клеткам
    for y in range(s1):
        if maze[x][y] == uv_unit_col: uv_units += 1

def setup():                # Тут, я думаю всё понятно
    global s1, s2
    size(s2 * s1 + 1, s2 * s1 + 1)

def draw():
    global d, state, exit_var, debounce_size, bX, bY, pFound, debounce, sX, sY, DBCs, s1, s2, black_col, white_col, red_col, orange_col, yellow_col, green_col, light_blue_col, blue_col, purple_col, bot_col, wall_col, uv_unit_col, v_unit_col, maze, uv_units
    for x in range(s1):         # Пробег по всем клеткам
        for y in range(s1):
            
            fill(maze[x][y])                               # Графика (Прорисовка, а не анимация)
            if maze[x][y] == white_col: stroke(0)
            else: stroke(white_col)
            rect(x * s2, y * s2, s2, s2)
            
            if DBCs[bX][bY] == 0:
                found = False
                direct = int(random(1, 5))
                if bX + 2 < s1 and maze[bX + 2][bY] == uv_unit_col and direct == 1:
                    maze[bX + 1][bY] = v_unit_col
                    maze[bX][bY] = v_unit_col
                    maze[bX + 2][bY] = bot_col
                    found = True
                    DBCs[bX + 2][bY] = d
                    bX += 2
                        
                elif bY + 2 < s1 and maze[bX][bY + 2] == uv_unit_col and direct == 2:
                    maze[bX][bY + 1] = v_unit_col
                    maze[bX][bY] = v_unit_col
                    maze[bX][bY + 2] = bot_col
                    found = True
                    DBCs[bX][bY + 2] = d
                    bY += 2
                        
                elif bX - 2 >= 0 and maze[bX - 2][bY] == uv_unit_col and direct == 3:
                    maze[bX - 1][bY] = v_unit_col
                    maze[bX][bY] = v_unit_col
                    maze[bX - 2][bY] = bot_col
                    found = True
                    DBCs[bX - 2][bY] = d
                    bX -= 2
                        
                elif bY - 2 >= 0 and maze[bX][bY - 2] == uv_unit_col and direct == 4:
                    maze[bX][bY - 1] = v_unit_col
                    maze[bX][bY] = v_unit_col
                    maze[bX][bY - 2] = bot_col
                    found = True
                    DBCs[bX][bY - 2] = d
                    bY -= 2
                        
                if found == False and debounce == 0:
                    maze[bX][bY] = v_unit_col
                    maze[sX][sY] = bot_col
                    exit_var = False
                    for x1 in range(s1):
                        if exit_var: break
                        for y1 in range(s1):
                            if exit_var: break
                            if maze[x1][y1] == uv_unit_col:
                                direct = int(random(1, 5))
                                if direct == 1 and x1 + 2 < s1 and maze[x1 + 2][y1] == v_unit_col:
                                    exit_var = True
                                    bX = x1 + 2
                                    bY = y1
                                    
                                elif direct == 2 and y1 + 2 < s1 and maze[x1][y1 + 2] == v_unit_col:
                                    exit_var = True
                                    bX = x1
                                    bY = y1 + 2
                                        
                                elif direct == 3 and x1 - 2 > -1 and maze[x1 - 2][y1] == v_unit_col:
                                    exit_var = True
                                    bX = x1 - 2
                                    bY = y1
                                        
                                elif direct == 4 and y1 - 2 > -1 and maze[x1][y1 - 2] == v_unit_col:
                                    exit_var = True
                                    bX = x1
                                    bY = y1 - 2
                    
                    
                if pFound != found: debounce = debounce_size
                pFound = found
                if debounce > 0: debounce -= 1
            if DBCs[x][y] > 0: DBCs[x][y] -= 1
            
            if keyPressed:
                for x1 in range(s1):
                    for y1 in range(s1):
                        if x1 % 2 != 0 and y1 % 2 != 0:
                            maze[x1][y1] = uv_unit_col
                        else: maze[x1][y1] = wall_col
                maze[sX][sY] = bot_col
                bX = sX
                bY = sY
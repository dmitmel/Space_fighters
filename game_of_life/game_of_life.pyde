s1x = 30
s1y = 30
s2 = 20

gen = []
next_gen = []
clicks = []

def grid_filler(sx, sy, grid, item):
    for x in range(sx):
        grid.append([])
        for y in range(sy):
            grid[x].append(item)

grid_filler(s1x, s1y, gen, 0)
grid_filler(s1x, s1y, next_gen, 0)
grid_filler(s1x, s1y, clicks, False)

zero = 50
one = 250
cell_stroke = 60
earsing = 0
adding = 1
changing = 2

kClick = False
generation = 0
population = 0
loadDelay = 0
maxLoadDelay = 40
maxFrames = 40
mouseMode = changing

for x in range(s1x):
    
    for y in range(s1y):
        
        if gen[x][y] == one:
            
            population += 1

def cell(x, y):
    global s1x, s1y, gen
    
    c = 0
    
    if x >= 0 and x < s1x:
        
        if y >= 0 and y < s1y:
            
            c = gen[x][y]
            
    return c
    
def neighbours(x, y):
    n = 0
    
    n += cell(x - 1, y)
    n += cell(x - 1, y + 1)
    n += cell(x, y + 1)
    n += cell(x + 1, y + 1)
    n += cell(x + 1, y)
    n += cell(x + 1, y - 1)
    n += cell(x, y - 1)
    n += cell(x - 1, y - 1)
    
    return n

def show():
    
    global s1x, s1y, s2, gen, next_gen, one, zero
    
    for x in range(s1x):
        
        for y in range(s1y):
            
            if gen[x][y] == 0:
                fill(zero)
                stroke(cell_stroke)
                
            else:
                fill(one)
                stroke(cell_stroke)
                
            rect(s2 * x, s2 * y, s2, s2)
            
    for x in range(s1x):
        
        for y in range(s1y):
            
            fill(128)
            
            textAlign(CENTER, CENTER)
            
            # text(neighbours(x, y), s2 * (x+0.5), s2 * (y+0.5))

def mouseDraw():
    global population, s1x, s1y, s2, gen, one, zero, next_gen, mouseMode, clicks, adding, earsing, changing
    
    if mousePressed:
        
        x = mouseX / s2
        
        y = mouseY / s2
        
        clicks[x][y] = True
        
        if mouseMode == changing:
            
            if gen[x][y] == 0:
               
                mouseMode = adding
            
            else:
                
                mouseMode = earsing
        
        if mouseMode == adding:
            
            next_gen[x][y] = 1
            
            population += 1
        
        else:
            
            next_gen[x][y] = 0
            
            population -= 1
   
    for x in range(s1x):
        
        for y in range(s1y):
            
            gen[x][y] = next_gen[x][y]
    
    show()

def countCells():
    
    population = 0
    
    for x in range(s1x):
        
        for y in range(s1y):
            
            if next_gen[x][y] == 1: population += 1
            
    return population
    
def keyMPressed(symbol):
    
    if keyPressed and key == symbol: return True
    else: return False

def setup():
    global s1x, s1y, s2
    
    size(s1x * s2 + 1, s1y * s2 + 1)
    
    show()
    
def draw():
    global s1x, s1y, s2, gen, next_gen, zero, one, state, maxLoadDelay, kClick, generation, population, loadDelay, maxloadDelay, maxFrames, mouseMode, changing
    
    mouseDraw()
    
    show()
    
    if not(mousePressed):
        
        for x in range(s1x):
            
            for y in range(s1y):
                
                if clicks[x][y]: clicks[x][y] = False
                
        mouseMode = changing
        
    if not(keyPressed):
        
        kClick = False
        
        loadDelay = 0
        
    if keyMPressed(' '): loadDelay += 1
    
    if loadDelay > maxLoadDelay: loadDelay = maxLoadDelay
    
    if keyMPressed(' ') and (not(kClick) or loadDelay > maxLoadDelay - 1):
        
        kClick = True
        
        if loadDelay > maxLoadDelay - 1:
            
            loadDelay = maxFrames
            
        generation += 1
        
        for x in range(s1x):
            
            for y in range(s1y):
                
                nCount = neighbours(x, y)
                
                next_gen[x][y] = gen[x][y]
                
                if nCount == 3:
                    
                    next_gen[x][y] = 1
                    
                elif nCount < 2 or nCount > 3:
                    
                    next_gen[x][y] = 0
                    
                if next_gen[x][y] == 0 and nCount == 3:
                    
                    population += 1
                    
                elif next_gen[x][y] == 1 and (nCount < 2 or nCount > 3):
                    
                    population -= 1
                    
    for x in range(s1x):
        
        for y in range(s1y):
            
            gen[x][y] = next_gen[x][y]
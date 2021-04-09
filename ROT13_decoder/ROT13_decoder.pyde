alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
moved = 'n o p q r s t u v w x y z a b c d e f g h i j k l m'.split(' ')
nums1 = {'1' : '1', '2' : '@', '3' : '#', '4' : '$', '5' : '%', '6' : '^', '7' : '&', '8' : '*', '9' : '(', '0' : ')'}
nums2 = '1 2 3 4 5 6 7 8 9 0'.split(' ')
click = False
leters = '_'
state = 1
wait = 0
capslock = False
rawLeters = ''
var = 0
def setup():
    size(900,900)
    
def draw():
    global alphabet, moved, click, leters, state, wait, rawLeters, capslock, var
    background(0)
    textSize(40)
    if not(keyPressed):
        wait = 0
        click = False
    if state == 1:
        fill(200)
        text('input:         (Press CTRL to decode)',50,60)
        text(str(leters),50,120,750,760)
        if capslock:
            fill('#0CA50A')
        else:
            fill('#D32000')
        text('CAPSLOCK',650,870)
        if keyPressed and wait < 40:
            wait += 1
        if keyPressed and frameCount % 3 == 0 and wait > 39:
            click = False
        if keyPressed and not(click) and key != BACKSPACE and keyCode != 17 and keyCode != 20 and keyCode != 16:
            leters = leters[:len(leters)-1]
            if str(key) in nums2:
                leters += nums1[int(key)]
            else:
                leters += str(key) + '_'
            click = True
        elif keyPressed and key == BACKSPACE and not(click):
            leters = leters[:len(leters)-2]
            leters += '_'
            click = True
        elif keyPressed and keyCode == 20 and not(click):
            capslock = not(capslock)
            click = True
        elif keyPressed and keyCode == 17 and not(click):
            state = 2
            click = True
    elif state == 2:
        leters = leters[:len(leters)-1]
        fill(200)
        for item in leters:
            if item.lower() in alphabet:
                if item == item.upper():
                    rawLeters += moved[alphabet.index(item.lower())].upper()
                else:
                    rawLeters += moved[alphabet.index(item)]
            else:
                rawLeters += item
        state = 3
    elif state == 3:
        fill(200)
        text('input:         (Press CTRL to return)',50,60)
        text(str(rawLeters),50,120,750,760)
        if keyPressed and keyCode == 17 and not(click):
            rawLeters = ''
            leters += '_'
            state = 1
            click = True

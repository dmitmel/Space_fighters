import easy_controls as ec
buttons = [ec.Text_button(), ec.Rect_button(), ec.Ellipse_button(), ec.Image_button()]
click = False

def setup():
    size(500, 500)
    buttons[0].custom(width / 2, height / 2 + 45)
    buttons[0].zone(250, 250, 335, 300)
    
    buttons[1].custom(100, 100, 100, 150)

    buttons[2].custom(400, 400, 100)
    
def draw():
    global click
    if not(mouseButton):
        click = False
    background(200)
    textSize(50)
    noFill()
    buttons[0].debug()
    buttons[0].show(mouseX, mouseY)
    rectMode(CENTER)
    buttons[1].show(mouseX, mouseY)
    buttons[2].show(mouseX, mouseY)
    if buttons[0].pressed(mouseX, mouseY) and not(click):
        print('One')
        click = True

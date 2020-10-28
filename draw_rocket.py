import turtle
t = turtle.Turtle()
def rocket_Body():
    '''none->none
        Draws the body of the rocket'''
    t.color("red", "blue")
    t.begin_fill()
    t.setpos(0, 0)
    t.left(90)
    t.forward(150)
    t.right(45)
    t.forward(58)
    circpos = t.position()
    t.right(90)
    t.forward(58)
    t.right(45)
    t.forward(150)
    sidepos = t.pos()
    t.right(90)
    t.goto(0, 0)
    t.end_fill()



def rocket_sides():
    '''none->none
        Draws the sides of the rocket'''
    t.color("blue", "red")
    t.goto(0, 70)
    t.begin_fill()
    for i in range(10):
        t.left(10)
        t.forward(10)
    t.forward(40)
    t.goto(0, 0)
    t.end_fill()
    t.up()
    t.goto(82.02, 70)
    t.down()
    t.left(90)
    t.begin_fill()
    for i in range(10):
        t.right(10)
        t.forward(10)
    t.forward(40)
    t.goto(82, 0)
    t.end_fill()


def rocket_window():
    '''none->none
        Draws the window of the rocket'''
    t.color("black", "white")
    t.up()
    t.goto(35, 120)
    t.down()
    for i in range(4):
        t.circle(7)
        t.up()
        t.forward(30)
        t.down()
    t.up()
    t.goto(6, 0)
    t.down()
    t.color("black", "yellow")
    t.begin_fill()


def thrusthers():
    '''none->none
        Draws the thrusters of the rocket'''
    t.penup()
    t.forward(10)
    t.down()
    for i in range(3):
        t.forward(20)
        t.left(90)
        t.forward(14)
        t.left(90)
        t.forward(20)
        if (i < 2):
            t.right(90)
            t.forward(12)
            t.right(90)
        if (i == 2):
            t.forward(10)
            for i in range(2):
                t.left(90)
                t.forward(66)
                t.left(90)
                t.forward(10)

    t.end_fill()
    t.ht()
def draw_rocket():
    '''none->none
        calls the predifined functions that draw all the parts of a rocket into one image'''
    t.speed(70)
    rocket_Body()
    rocket_sides()
    rocket_window()
    thrusthers()

draw_rocket()
################################################################################
# Description: Draws each letter on the screen sitting inside of bounding box
################################################################################

# Don't change this
from turtle import *

def draw_e():
    # Write this function
    #penup()
    #goto(-160, 30)
    pendown()
    forward(60)
    left(90)
    circle(30, 320)
    penup()

    return

def draw_h():
    # Write this function
    pendown()
    left(90)
    forward(120)
    backward(90)
    penup()
    #goto(-240,30)
    pendown()

    circle(-25, 180)
    forward(30)
    penup()

    return

def draw_l():
    # Write this function
    pendown()
    #left(90)
    forward(120)
    penup()

    return

def draw_o():
    # Write this function
    #penup()
    #goto(0, 0)
    pendown()
    circle(-30, 360)
    penup()
    #for i in range(25):
        #right(15)
        #forward(10)
    return

def draw_r():
    # Write this function
    pendown()
    #left(90)
    forward(60)
    backward(30)
    circle(-30, 90)
    penup()
    return

def draw_t():
    # Write this function
    pendown()
    left(90)
    forward(120)
    backward(30)
    left(90)
    forward(25)
    backward(50)
    penup()
    return

def draw_u():
    # Write this function
    pendown()
    #right(90)
    forward(60)
    backward(30)
    circle(30, -180)
    right(180)
    forward(30)
    penup()
    return

def main():

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------

    # Write your main function code here
    # hello part (top)
    penup()
    goto(-240,0)
    draw_h()

    penup()
    goto(-160, 30)
    left(90)
    draw_e()

    penup()
    left(40)
    goto(-60, 0)
    #towards(0, 100)
    draw_l()

    penup()
    goto(0, 0)
    draw_l()

    penup()
    goto(60, 30)
    draw_o()

    # turtle part (bottom)
    penup()
    goto(-240, -180)
    right(90)
    draw_t()

    penup()
    goto(-140, -180)
    right(90)
    draw_u()

    penup()
    goto(-100, -180)
    draw_r()

    penup()
    #right(90)
    goto(-30, -180)
    draw_t()

    penup()
    goto(30, -180)
    right(90)
    draw_l()

    penup()
    right(90)
    goto(60, -150)
    draw_e()

    #draw_t()
    #draw_l()
    #draw_e()

# Don't change this
if __name__ == '__main__':
    main()
    done()

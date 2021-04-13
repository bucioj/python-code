###############################################################################
# Author: Jose Bucio
# Date: 03/15/2021
# Description: Draws each vowel using turtle with specific coorindates and directions
###############################################################################

from turtle import *

def draw_a():
    pendown()
    left(90)
    forward(60)
    backward(30)
    circle(30)
    #right(90)
    backward(30)
    penup()
    home()
    #circle(30, -360)
    #return


def draw_e():
    penup()
    left(90)
    forward(30)
    right(90)
    pendown()
    backward(30)
    forward(60)
    left(90)
    circle(30, 325)
    penup()
    circle(30, 35)
    backward(30)
    home()

    #return

def draw_i():
    pendown()
    left(90)
    forward(50)
    x,y = pos()
    penup()
    goto(x, y+30)
    pendown()
    #forward(30)
    dot()
    penup()
    backward(80)
    home()
    #return

def draw_o():
    pendown()
    #circle(-30, 360)
    circle(30)
    #left(90)
    penup()
    home()
    #return

def draw_u():
    penup()
    #pendown()
    left(90)
    forward(60)
    pendown()
    #backward(30)
    right(180)
    forward(30)
    circle(30, 180)
    forward(30)
    backward(60)
    #right(90)
    #right(180)
    #forward(30)
    penup()
    home()
    #return

def main():

    # You can use this for your own testing.
    #width(9)
    #vowels = ['a', 'e', 'i', 'o', 'u']
    draw_a()
    draw_e()
    draw_i()
    draw_o()
    draw_u()

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()

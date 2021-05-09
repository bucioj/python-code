################################################################################
# Description: This program draws a sin and a cos graph using turtle graphics
################################################################################
from turtle import *
import math
#from math import *
#import math as m
import random as r

# Write function(s) here
#def drawCos:

#def drawSin:



def main():
    # Write your 'mainline logic' here
    line = Turtle()
    sinG = Turtle()
    cosG = Turtle()

    line.color('black')
    sinG.color('red')
    cosG.color('blue')

    line.speed(0)
    sinG.speed(0)
    cosG.speed(0)

    line.width(5)
    sinG.width(5)
    cosG.width(5)

    #graph = [drawCos, drawSin]

    #math.shuffle(graph)

    randInt = r.randint(60, 120)

    line.goto(0, 80)
    line.goto(0,-80)
    line.goto(0,0)
    line.goto(randInt * 4,0)


    for i in range(0, randInt, 1):
        sinG.goto(i * 4, 80 * math.sin(i/10))

    for i in range(0, randInt, 1):
        cosG.goto(i * 4, 80 * math.cos(i/10))

    cosG.hideturtle()
    sinG.hideturtle()
    line.hideturtle()




if __name__ == '__main__':
    main()
    done()

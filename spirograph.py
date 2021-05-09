###############################################################################
# This program makes a computerized version of a spirograph
###############################################################################

# imports
from turtle import *
from math import cos, sin, radians


def get_input():
    # the 3 apostrophes is a special type of comment called a doc string
    ''' Function to get user input '''
    R = int(input('Radius of larger circle: '))
    r = int(input('Radius of smaller circle: '))
    d = int(input('Distance from center of small circle: '))
    spins = int(input('Number of rotations: '))
    return R, r, d, spins


def get_point(angle, R, r, d):
    ''' Calculate the x and y values for the current point '''
    angle = radians(angle)
    x = (R - r) * cos(angle) + d * cos((R - r) / r * angle)
    y = (R - r) * sin(angle) - d * sin((R - r) / r * angle)
    return x, y


def main():
    # set up turtle
    setup(800, 800)
    speed(0)
    bgcolor('black')
    colormode(255)

    # spirograph parameters
    R, r, d, rotations = get_input()

    # go to starting point
    penup()
    start_x, start_y = get_point(0, R, r, d)
    goto(start_x, start_y)
    pendown()

    # run spirograph
    for angle in range(360):
        pencolor(angle * 255 // 360, 0, 255 - angle * 255 // 360)
        x, y = get_point(angle * rotations, R, r, d)
        goto(x, y)


if __name__ == '__main__':
    main()
    done()

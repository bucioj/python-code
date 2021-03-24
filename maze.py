################################################################################
# Description: Programs to move the turtle from the center of the maze to the exit
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # Write your code here
    # directions of the turle to exit maze
    forward(10)
    left(90)
    forward(35)
    right(90)
    forward(25)
    left(90)
    forward(75)
    left(90)
    forward(25)
    right(90)
    forward(95)
    right(90)
    forward(25)
    left(90)
    forward(25)
    right(90)
    forward(192)
    right(90)
    forward(230)
    left(90)
    forward(30)

    # options
    # forward() | backward() | right() | left() | goto() |
    # setx() sety() | setheading()
    # home() | circle() | dot() | stamp()


# Don't change this
if __name__ == '__main__':
    main()
    done()

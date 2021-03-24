################################################################################
# Description: Programs to draw the hex spiral start at 6 pixels
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    #screen = Screen()
    #t = Turtle()
    #screen.bgcolor('white')
    #t.speed(0)
    #t.forward(1)
    # forward(1)
    speed(0)
    for side in range(39):
        forward(side*6 + 6)
        right(60)
        #forward(side*6 + 6)

# Don't change this
if __name__ == '__main__':
    main()
    done()

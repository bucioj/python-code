###############################################################################
# Description: Create an arch spiral using radians and degrees with respect to x and y axis
###############################################################################
from turtle import *
from math import *

def main():
    # Don't change this block -------------------------------------------------
    setup(564, 564)
    width('5')
    # -------------------------------------------------------------------------


    # Write your mainline logic here ------------------------------------------
    #color("black")
    #down()
    #radius = 180
    #up()
    #radius = degrees * (pi/180)
    #for t in range(3):
        #x =
    #goto(0,0)
    #radians = (degress * pi) / 180
    down()
    speed(10)
    for degrees in range(2161):
        radians = (degrees / 180) * pi
        x = (degrees / 10) * cos(radians)
        y = (degrees / 10) * sin(radians)
        goto(x,y)
    up()

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()

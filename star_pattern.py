################################################################################
# Description: Programs to draw a star created given by specific # of points by user
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    #screen = Screen()
    num_point = int(input("Enter how many side points: "))
    #num_point = 8
    A = 360 / num_point
    B = 2 * A
    fillcolor('yellow')
    begin_fill()
    #inner_angle = star_angle * 2
    right((180 - B) / 2)

    speed(0)
    for i in range(num_point):
        forward(side_length)
        left(180 - A)
        forward(side_length)
        right(180 - B)
    end_fill()

# Don't change this
if __name__ == '__main__':
    main()
    done()

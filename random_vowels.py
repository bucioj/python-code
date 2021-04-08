###############################################################################
# Author: Jose Bucio
# Date: 03/15/2021
# Description: Allows to print all vowels in random order from vowels python file
###############################################################################

from turtle import *

# Add your imports here -------------------------------------------------------
import vowels
import random

def main():
    # Don't change this block -------------------------------------------------
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)
    # -------------------------------------------------------------------------


    # Write your mainline logic here ------------------------------------------
    # given coorindates from goto(-22,-30)
    x = -220
    y = -30

    # create a list of all vowels into a list
    vowel_list = [vowels.draw_a, vowels.draw_e, vowels.draw_i, vowels.draw_o, vowels.draw_u]

    # shuffle the list
    random.shuffle(vowel_list)

    # for loop for every letter
    for num in range(5):
        penup()
        goto(x,y)
        vowel_list[num]()
        pendown()

        # distance apart added with respect to x - axis for each letter
        x += 100

        #random.shuffle(vowel_list)
        #position()
        #print(vowel_list)
        #return

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()

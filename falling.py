################################################################################
#
# Description: Calculates the falling distance from 0 to 10 seconds
#
###############################################################################

# distance falling calculation
def falling_distance(time):
    #seconds = 0.0
    gravitational = 9.81 # gravitational force
    distance = 0.5 * gravitational * (time ** 2) # d = 1/2 gt^2
    return distance
# main
def main():
    print("Time (s)  Distance (m)\n----------------------")
    # print("-------------------------")
    for seconds in range(1, 11):
        distance_falling = falling_distance(seconds)
            #gravitational = 9.81
            #distance = 0.5 * gravitational * (time ** 2)
            #return distance
        print(format(seconds,'8,.0f'), format(distance_falling,'13,.2f'))
    # return distance

# Don't edit these 2 lines & make sure they're at the end of your program
if __name__ == '__main__':
    main() # calls the main function

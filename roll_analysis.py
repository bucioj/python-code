################################################################################
# Author: Jose Bucio
# Date: 03/15/2021
# Description: Determines the frequency for each sum of two six sided dice such
# that each die is rolled at random
################################################################################
import random

def main():
    size = 900000
    die_pair = get_2d6_rolls(size)

    # Output percentage
    print(f'Roll  Frequency')
    for roll_number in range(2,13):
        #print(f'{roll_number:3.0f} {percentage:8.2f}%')
        frequency = die_pair.count(roll_number) / size
        percentage = frequency * 100
        print(f'{roll_number:3} {percentage:8.2f}%')
    #for roll_number in number_rolls:
        #frequency = number_rolls[roll_number] / size
        #percentage = frequency * 100
        #(f'{roll_number:3.0f} {percentage.count(roll_number):8.2f}%')

# Single six-sided die rolled at random integer
def roll_d6():
    return random.randint(1,6)

# Simulate rolling two six sided dice from roll_d6 function
def get_2d6_rolls(roll_size):
    die_1 = []
    die_2 = []
    die_pair = []

    for number in range(roll_size):
        die_1.append(roll_d6())
        die_2.append(roll_d6())
        die_pair.append(die_1[-1] + die_2[-1])
        #die_1 = roll_d6()
        #die_2 = roll_d6()
        #total = die_1 + die_2
        #rolls[total] += 1
    return die_pair

if __name__ == '__main__':
    main()

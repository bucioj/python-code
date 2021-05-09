################################################################################
# Description: Programs to create a 6-, 10-, and 20-sided die and displays the results of rolling
################################################################################
import random

class Dice:
    # attribte sides & methods roll & n_rolls
    def __init__(self, sides):
        # sides attribute should stores the # of sides
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def n_rolls(self):
        return 10
        #list = []
        #for roll_num in range(10):
            #results = roll()
            #results.append(list)
        #return

def main():

    # 6 sided Die
    d6 = Dice(sides = 6)
    list = [] # creates a list
    # for every roll in 6 sided dice
    for num in range(d6.n_rolls()):
        result = d6.roll()
        list.append(result) # adds to list
    res = str(list)[1:-1]  # removes the brackets
    print(f'Rolling a 6 sided die 10 times: {res}')

    # 10 sided Die
    d10 = Dice(sides = 10)
    list = [] # list created
    # for every roll in 10 sided dice
    for num in range(d10.n_rolls()):
        result = d10.roll()
        list.append(result) # adds to list
    res = str(list)[1:-1] # removes the brackets
    print(f'Rolling a 10 sided die 10 times: {res}')

    # 20 sided Die
    d20 = Dice(sides = 20)
    list = [] # creates list
    # for every roll in 20 sided die
    for num in range(d20.n_rolls()):
        result = d20.roll()
        list.append(result) # adds to list
    res = str(list)[1:-1]  # removes the brackets
    print(f'Rolling a 20 sided die 10 times: {res}')

    #print(d6)

if __name__ == '__main__':
    main()

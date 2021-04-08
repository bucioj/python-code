###############################################################################
# Author: Jose Bucio
# Date: 03/11/2021
# Description: Displays a math quiz for user to enter answer and check user's answer is correct
###############################################################################
from random import randint

def main():

    number_1 = random_number(2)
    #number_1 = random.randrange(9, 99)
    number_2 = random_number(3)
    #number_2 = random.randrange(99, 999)

    print("   " + str(number_1))
    print("+ " + str(number_2))
    print("-----")
    #print(str(number_1) + "+ " + str(number_2) + " = ")

    # enter your answer
    result = int(input("= "))
    correct_result = str(number_1 + number_2)


    # Ouput based on your answer
    if result == (number_1 + number_2):
        print("Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {correct_result}.")

# random_number of digits
def random_number(digits):
    range_start = 10**(digits - 1)
    range_end = (10**digits) - 1
    return randint(range_start, range_end)



# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()

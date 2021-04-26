################################################################################
# Description: Programs to write random number for each line depending on user's
# input on how many numbers it should generate
################################################################################
import random

def main():
    # input a number from user
    user_input = int(input("Enter the number of random numbers to be written to the file: "))

    # prints the list of random numbers from user's input of lines
    # print(num_random(user_input))
    num_random(user_input)

# random numbers function
def num_random(user_input):
    # creates random_numbers.txt
    foo = open("random_numbers.txt", "a")

    # creates a list
    list = []
    for number in range(user_input):
        list.append(random.randint(1, 500))

    # list generation
    for number in list:
        # writes into the file random_numbers.txt
        foo.write(str(number))
        # new line created
        foo.write("\n")

    foo.close()
# returns a list of random numbers
    return list

if __name__ == '__main__':
    main()

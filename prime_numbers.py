################################################################################
# Description: Programs to determine which number is a prime number
###############################################################################
# Input
def get_input():
    number_input = int(input("Enter a positive integer (-1 to quit): "))
    return number_input

# Is Prime
def is_prime(number_input):
    # set prime to be true assume
    prime = True
    # when 1 is the number input
    if number_input == 1: prime = False
    # less than 4 (prime numbers 2 & 3)
    elif number_input < 4: prime = True # prime = True
    elif number_input % 2 == 0 or number_input % 3 == 0: prime = False
    else:
        for current_number in range(5, int(number_input**0.5)+1):
            if number_input % current_number == 0: prime = False
            if number_input % (current_number+2) == 0: prime = False
            current_number += 6
    return prime

# Main
def main():
    number_input = get_input()
    # number_input = int(input("Enter a positive interger (-1 to quit): "))
    if number_input == -1:
        return
    while number_input > 0:
        if is_prime(number_input):
            print(number_input, "is a prime number.")
            number_input = int(input("Enter a positive integer (-1 to quit): "))
        else:
            print(number_input, "is not a prime number.")
            number_input = int(input("Enter a positive integer (-1 to quit): "))
    return

# Don't edit these 2 lines & make sure they're at the end of your program
if __name__ == '__main__':
    main() # calls the main function

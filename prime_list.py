################################################################################
#
# Description: Programs allows to prime all prime numbers from a given number input
#
###############################################################################

def main():
    number_input = get_input()
    # print an entire list using
    # print(*a_list, sep=', ')
    # print the list without bracket
    #primes = display_output()
    primes = []
    for current_number in range(2, number_input+1):
        if is_prime(current_number):
            primes.append(current_number)
            #print(current_number, end=' ')
    #print(primes, sep=', ')
    print(f'The primes up to {number_input} are: ', end='')
    print(*primes, sep=', ')

def get_input():
    number_input = int(input("Enter a positive integer: "))
    return number_input

# Is Prime
def is_prime(number_input):
    # set prime to be true assume
    #prime_list = []
    prime = True
    # when 1 is the number input
    if number_input == 1: prime = False
    elif number_input == 2 or number_input == 3: prime = True
    #elif number_input < 4: prime = False
    # elif number_input == 2 or number_input == 3: prime = True
        #prime_list.append(number_input)
    elif number_input % 2 == 0 or number_input % 3 == 0: prime = False
    else:
        for current_number in range(5, int(number_input**0.5)+1):
            if number_input % current_number == 0: prime = False
            if number_input % (current_number+2) == 0: prime = False
            current_number += 6

            #return prime
    return prime

if __name__ == '__main__':
    main() # calls the main function

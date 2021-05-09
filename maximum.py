################################################################################
# Description: Programs to compare the two integers & see integer which is greater
###############################################################################
# Maximum between the two
def max_of_two(first_number, second_number):
    if first_number >= second_number:
        return first_number
    elif second_number >= first_number:
        return second_number
    else:
        return 0
        #return print("Both are equal.")

# Input
def get_input():
    user_first_number = int(input("Enter the first integer: "))
    user_second_number = int(input("Enter the second integer: "))
    return user_first_number, user_second_number

def main():
    # user_first_number, second_number = max_of_two()
    user_first_number, user_second_number = get_input()
    print(max_of_two(user_first_number, user_second_number), "is greater.")

# Don't edit these 2 lines & make sure they're at the end of your program
if __name__ == '__main__':
    main() # calls the main function

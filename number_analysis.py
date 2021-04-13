################################################################################
# Author: Jose Bucio
# Date: 03/15/2021
# Description: Analysis a number list from user's input to determine the lowest,
# highest, sum (total), and average number
################################################################################

def main():
    # take the list from get_number_list()
    number_list = get_number_list()

    # lowest number in list
    print(f'Lowest number: {min(number_list):.2f}')
    # highest number in list
    print(f'Highest number: {max(number_list):.2f}')
    # sum total of numbers in list
    print(f'Total: {sum(number_list):.2f}')
    # average of numbers in list
    print(f'Average: {sum(number_list) / len(number_list):.2f}')

    #return

# Creates a number list
def get_number_list():
    num_list = []
    total_list = 10
    for number in range(0,total_list):
        value = float(input(f'  Enter number {number+1:2.0f} of {total_list:1.0f}: '))
        num_list.append(value)

    # Collects tem floating point numbers from user and return a list
    return num_list

if __name__ == '__main__':
    main()

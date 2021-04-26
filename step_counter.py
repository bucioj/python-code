################################################################################
# Author: Jose Bucio
# Date: 03/30/2021
# Description: Calculates the average steps taken from user per month in one year
################################################################################

def main():
    # opens the file given
    file_name = open("steps.txt", 'r')

    steps = [] # declares list called steps
    # for each line in file_name
    for line in file_name:
        line = line.strip("\n") # next line
        if line != "": # not empty
            steps.append(int(line))
    file_name.close()
    # calculates the average steps per month
    average_steps(steps)

# average steps function
def average_steps(steps):
    print("The average steps taken each month were:")

    # declare months in list
    months_in_year = [("January", 31), ("February", 28), ("March", 31),
    ("April", 30), ("May", 31), ("June", 30), ("July", 31),
    ("August", 31), ("September", 30), ("October", 31),
    ("November", 30), ("December", 31)]
    #
    start = 0 # day 0
    # each month in year
    for month in months_in_year:
        total_steps = 0
        day = start # example day one for each month
        while day < (start + month[1]):
            total_steps = total_steps + steps[day]
            day += 1
        # calculates average steps per month
        average_steps = total_steps / month[1]
        #average_steps = f'total_steps / month[1]:.1f'
        print(month[0].rjust(10), ":", f'{average_steps:.1f}')
        #print(f"   {month[0]} : {average_steps:.1f}")
        # go to the next month
        start += month[1]

if __name__ == '__main__':
    main()

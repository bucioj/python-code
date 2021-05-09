################################################################################
# Description: Calculates the roulette color by given pocket number 
################################################################################

pocket_number = int(input("Please enter a pocket number: "))
# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
if pocket_number >= 0 and pocket_number <= 36:
    if pocket_number == 0:
        # Pocket 0 is green.
        pocket_color = "green"
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
    elif pocket_number >= 1 and pocket_number <= 10:
        if pocket_number % 2 == 0:
            pocket_color = "black"
        else:
            pocket_color = "red"

# For pockets 11 through 18, the odd-numbered pockets are black and even-numbered pockets are red.
    elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number % 2 == 0:
            pocket_color = "red"
        else:
            pocket_color = "black"
# For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.        elif pocket_number >= 19 && pocket_number <=28:
    elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number % 2 == 0:
            pocket_color = "black"
        else:
            pocket_color = "red"
# For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red.
    elif pocket_number >= 29 and pocket_number <= 36:
        if pocket_number % 2 == 0:
            pocket_color = "red"
        else:
            pocket_color = "black"
    #print "  Pocket " + pocket_number + "is " + pocket_color + "."
    #print(f"Pocket {pocket_number} is {pocket_color}.")

    print(f"  Pocket {pocket_number} is {pocket_color}.")

else:
        print("  Invalid Input!")

################################################################################
# Description: This program calculates sum & average from given number of inputs
################################################################################

user_input = float(input("Enter a non-negative number (negative to quit): "))

count, total = 0, 0
    #total += user_input
    # print("No input.")
if user_input >= 0:
    while user_input >= 0:
    #if user_input <= -1:
        #print("No input.")
        total += user_input
        count += 1
        user_input = float(input("Enter a non-negative number (negative to quit): "))
        #average = total / user_input
    print(f"Sum = {total:.2f}")
    average = float(total / count)
    print(f"Average = {average:.2f}")
    # total += user_input
    #if user_input <= -1:
        #total += user_input
        #print("No Input")
#average = total //
    #print(f"Sum = {total:.2f}")
else:
    print("No input.")

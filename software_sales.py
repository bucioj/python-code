################################################################################
# Description: Calculate the discount from given quantity
################################################################################

quantity = float(input("Please input the number of packages to be purchased: "))
discount = int()

if quantity > 0:
    # No discount applied less than 10
    if quantity < 10:
        print("  No discount applied.")
        discount = 1.0
# Discount applied 10 - 19 quantity
    elif quantity < 20:
        print("  10% discount applied.")
        discount = 0.90
# Discount applied 20 - 49 quantity
    elif quantity < 50:
        print("  25% discount applied.")
        discount = 0.75
# Discount applied 50 - 99 quantity
    elif quantity < 100:
        print("  35% discount applied.")
        discount = 0.65
# Discount applied 100 or more
    else:
        print("  45% discount applied.")
        discount = 0.55

    total_amount = quantity * discount * 99.0
    print(f'  The final price for purchasing {quantity:.0f} packages is ${total_amount:,.02f}.')
    #print "The final price for purchasing", quantity, "packages is $", total_amount, "."

else:
    # Other input 0 or less
    print("  Invalid Input!")

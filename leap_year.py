################################################################################
# This program calculates the leap year from given year
################################################################################

year = int(input("Please input a year: "))
# message = " "

#if year > 0:
    # divisible by 100
if year % 100 == 0:
    if year % 400 == 0:
        # iff also divisible by 400
        days = "29"
    else:
        days = "28"
else:
    # not divisible by 100 but iff divisible by 4
    if year % 4 == 0:
        days = "29"
    else:
        days = "28"
print(f"In the year {year}, there are {days} days in February.")
    #message += " days in February."

################################################################################
#
# Program to collect data & calculate average rainfall
# over a period of years
################################################################################

#Input Number of years
years = int(input("Enter the number of years: "))
total_months = 0
total_rainfall = 0.0
average_rainfall = 0.0
if years >= 1:
    for current_year in range(1, years + 1):
        month = ['Jan.: ', 'Feb.: ', 'Mar.: ', 'Apr.: ', 'May.: ', 'Jun.: ', \
    'Jul.: ', 'Aug.: ', 'Sep.: ', 'Oct.: ', 'Nov.: ', 'Dec.: ']
        print(f"  For year No. {current_year}")
        #while monthly_rainfall > 0:
        for current_month in month:
                # print(f"For year No. {years}")
            monthly_rainfall = float(input("    Enter the rainfall for " + format(current_month)))
            while monthly_rainfall < 0:
                print("    Invalid input, please try again.")
                monthly_rainfall = float(input("    Enter the rainfall for " + format(current_month)))
            total_rainfall += monthly_rainfall
            total_months += 1

    average_rainfall = total_rainfall / total_months
    print(f"There are {total_months} months.")
    print(f"The total rainfall is {total_rainfall:.2f} inches.")
    print(f"The monthly average rainfall is {average_rainfall:.2f} inches.")

else:
    print("Invalid input.")

# total = 0.0
# average = 0.0

# years = 0
# month = 0.0
# total_months = 0

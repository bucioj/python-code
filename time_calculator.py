################################################################################
# Description: This program calculates the roulette color by given pocket number
################################################################################

number_of_seconds = int(input("Please enter a time in seconds. "))
days = int(number_of_seconds // 86400)
hours = int((number_of_seconds % 86400) // 3600)
minutes = int(((number_of_seconds % 86400) % 3600) // 60)
seconds = int(((number_of_seconds % 86400) % 3600) % 60)
# print(f"  {number_of_seconds:,.0f} seconds is: ", end="")
# less than 1 minutes

if number_of_seconds >= 0 and number_of_seconds < 60:
    print("  The number of seconds is less than one minute.")
# more than 1 minute and less than 1 hour
elif number_of_seconds >= 60 and number_of_seconds < 3600:
    print(f"  {number_of_seconds:,.0f} seconds is: ", end="")
    if seconds % 60 == 0:
        print(f"{minutes} minute(s).")
    else:
        print(f"{minutes} minute(s) and {seconds} second(s).")

# more than 1 hour and less than 1 day
elif number_of_seconds >= 3600 and number_of_seconds < 86400:
    print(f"  {number_of_seconds:,.0f} seconds is: ", end="")
    print(f"{hours} hour(s)", end="")
    if minutes and seconds:
        print(f", {minutes} minute(s) and {seconds} second(s)", end="")
    elif minutes:
        print(f" and {minutes} minute(s)", end="")
    elif seconds:
        print(f" and {seconds} second(s)", end="")
    print(".")

# more than 1 day
elif number_of_seconds >= 86400:
    print(f"  {number_of_seconds:,.0f} seconds is: ", end="")
    print(f"{days} day(s)", end="")
    if hours:
        if minutes and seconds:
            #print(f"{hours} hour(s),", end="")
            print(f", {hours} hour(s), {minutes} minute(s) and {seconds} second(s)", end="")
        elif hours and minutes:
            # print(f" {hours} hour(s),", end="")
            print(f", {hours} hour(s) and {minutes} minute(s)", end="")
        elif hours and seconds:
            # print(f" {hours} hour(s)", end="")
            print(f", {hours} hour(s) and {seconds} second(s)", end="")
        else:
            print(f" and {hours} hour(s)", end="")
#minutes or seconds (or both)
    elif minutes and seconds:
        print(f", {minutes} minute(s) and {seconds} second(s)", end="")
    elif minutes:
        print(f" and {minutes} minute(s)", end="")
    elif seconds:
        print(f" and {seconds} second(s)", end="")
    print(".")
# less than 60 seconds
#else:
    #print("  The number of seconds is less than one minute.")

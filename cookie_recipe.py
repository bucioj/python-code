# Determines total amount of sugar, butter & flour of many cookies a user wants

#1. Input
number_of_cookies = int(input('How many cookies do you want to make? '))

#2. Process
COOKIES = 48
SUGAR = 1.5
BUTTER = 1.0
FLOUR = 2.75

total_sugar = (SUGAR * number_of_cookies) / COOKIES
total_butter = (BUTTER * number_of_cookies) / COOKIES
total_flour = (FLOUR * number_of_cookies) / COOKIES

#3. Output
# message = 'To make ' + str(number_of_cookies) + ' cookies, you will need:'
# print(message)
print(f'To make {number_of_cookies} cookies, you will need:')

# message = "   " + format(total_sugar, '.2f') + " cups of sugar"
#print(message)
print(f'{total_sugar:7.2f} cups of sugar')
# print(" ",format(total_sugar, '.2f'), " cups of sugar")

#message = "   " + format(total_butter, '.2f') + " cups of butter"
#print(message)
# print(" ",format(total_butter, '.2f'), " cups of butter")
print(f'{total_butter:7.2f} cups of butter')

#message = "  " + format(total_flour, '.2f') + " cups of flour"
#print(message)
# print(" ",format(total_flour, '.2f'), " cups of flour")
print(f'{total_flour:7.2f} cups of flour')

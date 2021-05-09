###############################################################################
# This program asks a user what their pizza budget is and displays a list of
# all pizzas within their budget
###############################################################################

# list pizza options
sizes = ['small','medium','large']
crust_options = ['thin', 'garlic', 'pan', 'stuffed']
toppings = ['pepperoni','tomatoes','sausage']
meats = ['pepperoni', 'sausage']

# base pizza costs
small_cost = 10
med_cost = 12
large_cost = 14

# additional costs
stuffed_add = 1.5 # additional cost for stuffed crust
meat_add = .5 # additional cost for meat topping

# collect user input
while True:
    budget = float(input('Enter your budget for pizza: '))
    # test for valid input
    if budget < 0:
        print('Invalid input!')
    else:
        break # exit the while loop once valid input is received

# print table header
print('Size    | Crust   | Topping   | Cost')
print('---------------------------------------')

printed = False # initialize print flag

# calculate pizza cost and display if less than user's budget
for size in sizes:
    for crust in crust_options:
        for topping in toppings:
            # set initial cost based on size
            if size == 'small':
                cost = small_cost
            elif size == 'medium':
                cost = med_cost
            else:
                cost = large_cost

            # check for stuffed crust
            if crust == 'stuffed':
                cost += stuffed_add

            # check if the current topping is in the list "meats"
            if topping in meats:
                cost += meat_add

            # display pizza options in user's budget
            if cost <= budget:
                print(f'{size:<7} | {crust:<7} | {topping:<9} | ${cost:.2f}')
                printed = True # set printed flag to true if there was a pizza in the user's budget

# if no pizzas were in the user's budget, display message
if printed == False:
    print('No pizzas in your budget :(')

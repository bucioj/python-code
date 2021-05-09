###############################################################################
# This program creates a shopping list and calculates the estimated cost for
# for roommates buying shared items
###############################################################################

def load_dict():
    """function to load dictionary from csv file"""
    price_guide = {}
    with open('prices.csv', 'r') as f:
        next(f)
        for line in f:
            item, price = line.strip().split(',')
            price_guide[item] = int(price)

    return price_guide

def get_user_list(price_guide):
    """function to collect shopping list from user"""
    user_list = []
    while True:
        item = input('Enter list item (done to exit): ')
        if item == 'done':
            return set(user_list)
        elif item not in price_guide:
            print('  ERROR: no pricing information for that item')
        elif item in user_list:
            print('  ERROR: item already in list!')
        else:
            user_list.append(item)
            print('------------------------')
            print('Current shopping list:')
            for item in user_list:
                print(f'  - {item}')
            print('------------------------')

def calc_price(user_list, price_guide):
    """function to calculate total price of a set of items"""
    cost = 0
    for item in user_list:
        cost += price_guide[item]

    return cost

def display_guide(price_guide):
    """function to display the price guide"""
    print('====================================')
    print('PRICING GUIDE')
    for k in price_guide:
        print(f'  {k:>12}: ${price_guide[k]}')
    print('====================================')

def main():
    # create the price guide dictionary
    price_guide = load_dict()

    # display the price guide
    display_guide(price_guide)

    # get shopping lists for each roommate
    print('First roommate shopping list:')
    user_list1 = get_user_list(price_guide)

    print('Second roommate shopping list:')
    user_list2 = get_user_list(price_guide)

    # calculate cost of items ONLY user 1 wants
    roommate1 = user_list1 - user_list2
    roommate1_cost = calc_price(roommate1, price_guide)
    print(f'Roommate 1 cost = ${roommate1_cost}')

    # calculate cost of items ONLY user 2 wants
    roommate2 = user_list2 - user_list1
    roommate2_cost = calc_price(roommate2, price_guide)
    print(f'Roommate 2 cost = ${roommate2_cost}')

    # calculate cost of items BOTH user 1 and 2 want
    roommate_list = user_list1 & user_list2
    shared_cost = calc_price(roommate_list, price_guide)
    print(f'Shared cost = ${shared_cost}')

if __name__ == '__main__':
    main()

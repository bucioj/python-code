###############################################################################
# This program runs a simulation of two coffee shops and compares their average
# service times
###############################################################################
'''
Notes for this project:
- this project uses discrete event simulation which models the operation of a 
  system as a sequence of events in time
- each event occurs at a particular instant in time and marks the change of 
  state of a system
- we use an exponential distribution which is the probability distribution of 
  the time between events in a Poisson process
'''


import random as r


class CoffeeShop:
    '''A class to create the occee shop entity'''

    def __init__(self, name, num_baristas=2, cust_per_hr=10):
        self.name = name
        self.cust_per_hr = cust_per_hr

        # create a list of instances of the Barista class for each barista
        self.baristas = []
        for i in range(num_baristas):
            self.baristas.append(Barista())

    def run_sim(self, num_hours=8):
        '''A method to run the coffee shop simulation on an instance of CoffeeShop'''
        time_in_sys = []  # list of amounts of time customers spent in the system
        t = 0  # initialize current time to 0
        while t <= num_hours:
            # get arrival time of customer
            t += r.expovariate(self.cust_per_hr)

            # create an instance of Customer with specified arrival time
            cust = Customer(t, self)
            done = cust.order_drink()  # get what time the customer's drink is completed

            # calculate amount of time
            time_in_sys.append(done - t)

        # display coffee shop's statistics
        num_cust = len(time_in_sys)
        avg_time = sum(time_in_sys) / len(time_in_sys)
        print(f'  Number of customers served: {num_cust}')
        print(f'  Average time in sys: {avg_time:.2f} minutes')

        return avg_time

    def get_drink(self, start_time):
        # find which barista will be available next
        # initialize to none and a very large number
        first_available, min_so_far = None, 999

        # check each barista's "next_available" attribute to find the smallest
        for barista in self.baristas:
            # if the barista has the smallest "next_available" time so far,
            # set that barista as the first available
            if barista.next_available < min_so_far:
                first_available = barista
                min_so_far = barista.next_available

        # call the "make coffee" method on the first available barista
        end_time = first_available.make_coffee(start_time)

        return end_time


class Barista:
    def __init__(self):
        self.next_available = 0  # time barista is next available

    def make_coffee(self, start_time):
        '''method for Barista to make coffee
        input: start_time = when the customer orders the coffee
        output: next_availabe = time barista finishes making coffee'''

        # get how long it takes the barista to make the coffee
        time = r.expovariate(3)  # average of 3 minutes to make coffee

        # update barista's next available time (aka when the coffee is done)
        # if barista is NOT busy when the customer arrives, start making coffee immediately
        # if barista IS busy, start making coffee as soon as barista is available
        self.next_available = max(start_time, self.next_available) + time

        return self.next_available


class Customer:
    def __init__(self, arrival, coffee_shop):
        self.arrival = arrival  # time arrived at coffee shop

        # instance of coffee shop the customer is ordering from
        self.coffee_shop = coffee_shop

    def order_drink(self):
        '''Method for customer to order a drink'''
        return self.coffee_shop.get_drink(self.arrival)


def main():
    # create coffee shops
    ShopA = CoffeeShop('Shop A', 2, 12)  # 2 baristas, 12 cust/hr
    ShopB = CoffeeShop('Shop B', 3, 20)  # 3 baristas, 20 cust/hr

    # run the simulation and get the average time the customer spends in each shop
    print('ShopA:')
    avg_timeA = ShopA.run_sim()

    print('ShopB:')
    avg_timeB = ShopB.run_sim()

    # compare shops
    if avg_timeA < avg_timeB:
        print(f'{ShopA.name} is faster.')
    else:
        print(f'{ShopB.name} is faster.')


if __name__ == '__main__':
    main()

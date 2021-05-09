################################################################################
# Author: Jose Bucio
# Date: 04/15/2021
# Description: Reads the weekly average gas prices in the U.S and plots as a line
# graph during the year 2008
################################################################################
import matplotlib.pyplot as plt

def main():

    # declares the axis list
    x_axis = [] # x axis
    y_axis = [] # y axis

    # open file given
    file = open("2008_Weekly_Gas_Averages.txt")
    lines = file.readlines() # read the lines
    # for every x & y, add value
    for x, y in enumerate(lines):
        x_axis = x_axis + [x] # add index to x
        y_axis = y_axis + [float(y.strip())] # add y value
    file.close()

    plt.plot(x_axis, y_axis) # plot the graph
    plt.grid() # create a grid

    #start from 0 at left bottom corner
    #plt.axis([0, 52, 1.5, 4.25])
    plt.xlim([1, 52])
    plt.ylim([1.5, 4.25])

    # x & y label
    plt.xlabel("Weeks (by number)")
    plt.ylabel("Average Price (dollars/gallon)")

    # develop a title & save pdf file
    plt.title("2008 Weekly Gas Prices")
    plt.savefig("gas_prices.pdf")
    #plt.show() # show the grid created

if __name__ == '__main__':
    main()
    plt.show()

################################################################################
# Author: Jose Bucio
# Date: 04/15/2021
# Description: Collects monthly sales data from user, store in a list and plot
# the sales values as pie chart (one color of pie slice represents month)
################################################################################
import matplotlib.pyplot as plt

def main():
    # set the sales to zero
    sales = [0,0,0,0,0,0,0,0,0,0,0,0]

    # declare list of months of the year
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December']

    # delare list of colors from its hex code
    colors = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A',
    '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A']

    # input the number of sales per month
    sales[0] = int(input(f'Enter the sales for {months[0]}: ')) # January
    sales[1] = int(input(f'Enter the sales for {months[1]}: ')) # February
    sales[2] = int(input(f'Enter the sales for {months[2]}: ')) # March
    sales[3] = int(input(f'Enter the sales for {months[3]}: ')) # April
    sales[4] = int(input(f'Enter the sales for {months[4]}: ')) # May
    sales[5] = int(input(f'Enter the sales for {months[5]}: ')) # June
    sales[6] = int(input(f'Enter the sales for {months[6]}: ')) # July
    sales[7] = int(input(f'Enter the sales for {months[7]}: ')) # August
    sales[8] = int(input(f'Enter the sales for {months[8]}: ')) # September
    sales[9] = int(input(f'Enter the sales for {months[9]}: ')) # October
    sales[10] = int(input(f'Enter the sales for {months[10]}: ')) # November
    sales[11] = int(input(f'Enter the sales for {months[11]}: ')) # December

    # plot the pie chart
    plt.pie(sales, colors = colors, labels = months)
    plt.title("Monthly Sales Values") # title of the plot
    plt.savefig("monthly_sales.pdf") # store and save the plot into pdf file
    # plt.show() # show plot

if __name__ == '__main__':
    main()
    plt.show()

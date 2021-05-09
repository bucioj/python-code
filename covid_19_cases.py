################################################################################
# Description: Creates a bar chart on the spread of covid-19 disease in the state
# of Indiana as of April 4 2021
################################################################################
import datetime
import numpy as np
import matplotlib.pyplot as plt

def main():
    # with open('indiana_covid_19_data.txt', 'r') as file:
    file = open("indiana_covid_19_data.txt" , "r")
    # declare dictionaries dates and position
    dates = []
    position = []

    # for every line from file
    for line in file:
        #split the text for reach line
        words = line.split(" ")

        # include first column and third column from text file
        dates.append(datetime.datetime.strptime(words[0], '%Y-%m-%d').date())
        
        #dates.append(datetime.datetime.strptime(words[0], '%Y-%m').date())
        position.append(float(words[2]))
    # sets cumulative positive cases for each day
    position = np.cumsum(position)

    #create bar graph
    plt.bar(dates, position)
    #plt.xlim([0, max(x_axis)])
    plt.ylim([0, 800])

    # set tick marks for each axis
    plt.xticks(np.arange(dates[9], dates[-1], datetime.timedelta(days=60)), rotation=30)
    plt.yticks(np.arange(0, position[-1], 100))

    # labels to bar graph
    plt.title('Positive COVID-19 Cases in Indiana')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases (in thousands)')
    # save into pdf file
    plt.savefig("covid_19_cases.pdf")
    # close files before exit
    file.close()
    #plt.show()

if __name__ == '__main__':
    main()
    plt.show()

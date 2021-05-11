###############################################################################
# Description: Programs to count # of times each letters in in file & plots bar
# chart of the letter used frequently
###############################################################################
import matplotlib.pyplot as plt

def main():
    # open the file
    file = open('phrases.txt')
    text = file.read()
    total_length = 0 # total length of the titles
    # set list of letters of the alphabet with their frequency
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    count_letter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #for char in file.read():
    for char in text: # for every letter from text
        uppercase_letter = char.upper()
        for letter in uppercase_letter: # for every letter from uppercase letter
            if letter.isalpha():
                count_letter[ord(letter) - 65] = count_letter[ord(letter) - 65]+1
                total_length += 1
        #count_letter[char.upper()] = 0
    #file = open('phrases.txt')
    #for line in file.read():
        #count_letter[line.upper()] = count_letter[line.upper()]+1
    # record the frequency
    frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for count in range(0, len(count_letter)):
        frequency[count] = count_letter[count] / total_length
    file.close()
    #x_axis = [] # #y_axis = [] # #total = 0 # #frequency = []
    #for key, value in count_letter.items():
        #x_axis.append(key)
        #y_axis.append(value)
    #for y_i in y_axis:
        #total += y_i
    #for y_j in y_axis:
        #frequency.append(y_j/total)
    # creates bar graph
    plt.bar(alphabet, frequency)
    # sets the labels
    plt.title('Letter Frequency in Puzzle Phrases') # title name
    plt.xlabel('Letter') # x axis label
    plt.ylabel('Letter Appearance Frequency') # y axis label
    # creates the grid to the bar graph
    plt.grid(axis = 'both') # add gridlines
    # save file in pdf
    plt.savefig('wof_analysis.pdf') # save file
    #file.close()

if __name__ == '__main__':
    main()
    plt.show()

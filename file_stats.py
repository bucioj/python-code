################################################################################
# Author: Jose Bucio
# Date: 03/30/2021
# Description: Programs to read the content from text file, tracks number of
# words, lines, and average number of words per line
################################################################################

def main():
    # get file name given
    file_name = "rumpelstiltskin.txt"

    # set word and line declare
    line_count = 0
    word_count = 1 # Start first word
    word_list = []

    # open the file
    with open(file_name) as foo: # declare file_name as fo
        line = foo.readline()

        # read line by line
        while line:
            line_count += 1 # line count one by one
            line = foo.readline()
            # split word list
            word_list = line.split()
            # increment word count with word length for each line
            word_count += len(word_list)

    # prints the results
    print(f"Total number of words: {word_count}")
    print(f"Total number of lines: {line_count}")

    # calculate the average words per line
    average = word_count / line_count
    # prints the average words per line
    print(f"Average number of words per line: {average:.1f}")

if __name__ == '__main__':
    main()

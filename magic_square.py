################################################################################
# Description: Determines whether a given square table is a Lo Shu Magic square
# meaning sum of each row, each column, and each diagonal all add up to 15
################################################################################

def main():

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #m1 = [[4,2,9], [8,6,1],[3,7,5]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    #print(f'Your square is:')
    result = is_magic(m1)
    if result == True:
        print('It is a Lo Shu magic square!\n')
    elif result == False:
        print('It is not a Lo Shu magic square.\n')

    #print(f'Your square is:')
    result = is_magic(m2)
    if result == True:
        print('It is a Lo Shu magic square!\n')
    elif result == False:
        print('It is not a Lo Shu magic square.\n')

    #print(f'Your square is:')
    result = is_magic(m3)
    if result == True:
        print('It is a Lo Shu magic square!\n')
    elif result == False:
        print('It is not a Lo Shu magic square.\n')

    #print(f'Your square is:\n{result}')
    #is_magic(m1)
    #print('')

    #print_square(m2)
    #print(f'Your square is:\n{result}')
    #is_magic(m2)
    #print('')

    #print_square(m3)
    #print(f'Your square is:\n{is_magic(m3)}')
    #is_magic(m3)

# Takes 2-D list of nums as arguments and prints a 3-by-3 grid showing numbers
def print_square(square):
    print('Your square is:')
    # checks matrix
    # prints the matrix
    for row in range(len(square)): # prints row
        #print(f'{row}', end=' ')
        for column in range(len(square[row])): # prints column
            print(f'{square[row][column]}', end=' ')
            #print(f'{column}', end=' ')
        print('')
    #print(' ')

    # checks for duplicates (row & column) of a given matrix
    for row in range(len(square)): # checks row
        for column in range(len(square[row])): # checks column
            if square[row][column] == square[row][column - 1]:
                return False
        if square[row][column] == square[row - 1][column]:
            return False

    # checks to see the square is Lo Shu
    for row in square:
        for column in range(3):
            if sum(row) == sum(square[column][column] for column in range(3)):
                    if sum(row) == sum(row[column] for i in square):
                    # yes for Lo Shu
                        return True
            else:
                return False
    #return

# returns True if argument represents Lo Shu Magic
def is_magic(square):
    if(print_square(square) == True):
        #print('It is a Lo Shu magic square!\n')
        result = True
    else:
        #print('It is not a Lo Shu magic square.\n')
        result = False
    return result

if __name__ == '__main__':
    main()

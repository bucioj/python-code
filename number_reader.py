################################################################################
# Description: Determines the maximum, minimum, sum, and average from the file
# random_numbers.txt created
################################################################################

def main():
    # get file generated from previous exercise
    file_name = "random_numbers.txt"
    # delare variables
    count_num = 0 # declare number count to 0
    min_number = int() # declare minimum
    max_number = int() # declare maximum
    total = 0 # declare sum

    # open file
    with open(file_name, 'r') as foo:
        # for each line in text file
        for line in foo:
            num = int(line.strip())
            # determines the maximum and minimum number
            if count_num == 0:
                min_number = max_number = num
            elif min_number > num:
                min_number = num
            elif max_number < num:
                max_number = num
            # keeps track of sum and list number of count
            total += num
            count_num += 1
    # prints the total numbers from the text file
    print(f"{count_num:,} numbers were read from the file.")
    # prints maximum number
    print(f"Max: {max_number}")
    # prints minimum number
    print(f"Min: {min_number}")
    # prints the sum
    print(f"Sum: {total:,}")
    # calulates and prints the average
    average = total / count_num
    print(f"Avg: {average:.1f}")

if __name__ == '__main__':
    main()

################################################################################
# Description: Programs to determine the list of multiples of 7 from given list
################################################################################

def main():
    #print("Original list of numbers:")
    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406]
    print(f'Original list of numbers:')
    print(number_list)
    #print("Original list of numbers:\n{}".format(number_list))

    multiple = 7
    multiples_of(multiple, number_list)
    print(f"Numbers in the list that are multiples of {multiple}:")
    print(number_list)
    #multiple, number_list = multiples_of(number, list)
    #print(multiples_of(number, list))

# find the multiples from a given list
def multiples_of(multiple_number, number_list):
    #pivot = 0
    for index in range(len(number_list)-1, -1, -1):
        if number_list[index] % multiple_number != 0:
            number_list.pop(index)
    #for index in number_list:
        #if index % multiple_number == 0:
            #number_list.remove(index)
            #number_list.extend(index)
    return number_list

if __name__ == '__main__':
    main()

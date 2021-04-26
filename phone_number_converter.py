################################################################################
# Author: Jose Bucio
# Date: 03/30/2021
# Description: Programs collect a phone-number string of words and convert into
# numbers only
################################################################################

def main():
    # input phone number from user
    phone_number = input("Enter a telephone number: ")

    # phone number convert all uppercase
    phone_number = phone_number.upper()

    # print phone converter
    num = convert_number(phone_number)
    print(f"The phone number is {num}")

# convert number function
def convert_number(phone_number):
    new_number = ""
    for char in phone_number:
        letter = char
        # each letter represents a specific number
        if str.isalpha(letter):
            # Digit 2
            if letter == "A" or letter == "B" or letter == "C":
                letter = str(2)
            # Digit 3
            elif letter == "D" or letter == "E" or letter == "F":
                letter = str(3)
            # Digit 4
            elif letter == "G" or letter == "H" or letter == "I":
                letter = str(4)
            # Digit 5
            elif letter == "J" or letter == "K" or letter == "L":
                letter = str(5)
            # Digit 6
            elif letter == "M" or letter == "N" or letter == "O":
                letter = str(6)
            # Digit 7
            elif letter == "P" or letter == "Q" or letter == "R" or letter == "S":
                letter = str(7)
            # Digit 8
            elif letter == "T" or letter == "U" or letter == "V":
                letter = str(8)
            # Digit 9
            elif letter == "W" or letter == "X" or letter == "Y" or letter == "Z":
                letter = str(9)
        # convert each char into number
        new_number = new_number + letter
    # return the new number or number converter
    return new_number

if __name__ == '__main__':
    main()

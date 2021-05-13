###############################################################################
# Description: Programs to play Wheel of Fortune for a single player with four rounds
###############################################################################
import random
## displays the game
def game_display(round, phrase, vowels, consonants, earnings):
    print(f':::::::::::::::::::::::::::::::::::::::::: ROUND {round} of 4 ::') #
    print(f'::', phrase.center(52), '::')
    print(f'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    consonants = get_string(consonants) # consonant
    vowels = get_string(vowels) # vowels
    print(f'::  ', consonants.ljust(5), '  ::  ', vowels.rjust(5) + '   :: ', f'${earnings:,}'.rjust(9), '::')
    print(f'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
# get phrases from given text file
def get_phrases():
    with open('phrases.txt') as file:
        file_stored = file.readlines()
        file.close()
    return file_stored
# random phrases function
def random_phrase(file_stored):
    phrase = random.choice(file_stored)
    original_string = phrase
    #original_string = random.choice(file_stored)
    new_string = []
    copy_string = phrase
    for letter in list(copy_string):
        new_letter = letter
        if letter.isalpha():
            new_letter = '_'
        new_string.append(new_letter)
    return new_string, original_string
# get string function
def get_string(list):
    create_string = ""
    for letter in list:
        create_string += letter
    return create_string
# user input function
def user_input():
    # prints the list of options
    print('What would you like to do?')
    print('  1 - Spin the wheel')
    print('  2 - Buy a vowel')
    print('  3 - Solve the puzzle')
    print('  4 - Quit the game')
    response = input('Enter the number of your choice: ')
    return response # return the user response
# spin the wheel function
def spin_the_wheel():
    spin_list = [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700, 800, 900, 2500, 'BANKRUPT', 'BANKRUPT']
    spin = random.choice(spin_list)
    return spin # return the price from spin the wheel
# list of vowels
def vowel_list():
    # vowels provided for game screen
    vowels = ['A', 'E', 'I', 'O', 'U']
    return vowels
# list of consonants
def consonant_list():
    # consonant provided for game screen
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    return consonants
# choose consonant function
def choose_consonant(consonant_choice, consonant_used):
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    # possible options when user picked a consonant or not
    if len(consonant_choice) > 1: # provides more than one letter
        print(f'Please enter exactly one character.')
        return 0 # return false
    elif (consonant_choice.upper() == 'A') or (consonant_choice.upper() == 'E') or (consonant_choice.upper() == 'I') or (consonant_choice.upper() == 'O') or (consonant_choice.upper() == 'U'):
        print('Vowels must be purchased.') # input a vowel
        return 0 # return false
    elif consonant_choice.isalpha() == 0:
        print(f'The character {consonant_choice} is not a letter.') # input not a letter
        return 0 # return false
    elif (consonant_choice.upper() in consonant_used) and (consonant_choice.upper() in consonants):
        print(f'The letter {consonant_choice.upper()} has already been used.') # input already used before
        return 0 # return false
    elif (consonant_choice.upper() in consonants) and (consonant_choice.upper() not in consonant_used):
        return 1 # return true
#    return
# get new phrase after each round
def get_new_phrase(consonant_choice, original, updated_string):
    original = list(original)
    for letter in range(len(original)):
        if (original[letter] == consonant_choice) or (original[letter] == consonant_choice.upper()):
            updated_string[letter] = consonant_choice.upper()
    return updated_string
# choose vowel function
def choose_vowel(vowel_choice, vowels):
    is_vowel = 0
    all_vowels = ['A', 'E', 'I', 'O', 'U'] # list of vowels
    all_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    #vowels = vowel_list()
    #consonants = consonant_list()
    if (vowel_choice.upper() in all_vowels) and (vowel_choice.upper() in vowels):
        is_vowel = 1
    # possible options when a user choose a vowel or not
    elif vowel_choice.upper() in all_consonants:
        print('Consonants cannot be purchased.') # user choose consonant
    elif len(vowel_choice) > 1:
        print('Please enter exactly one character.') # input is more than one letter
    elif vowel_choice.isalpha() == 0:
        print(f'The character {vowel_choice} is not a letter.') # input is not a letter
    elif (vowel_choice.upper() not in vowels) and (vowel_choice.isalpha()) and (vowel_choice.upper() in all_vowels):
        print(f'The letter {vowel_choice.upper()} has already been purchased.')
    elif len(vowels) == 0:
        print('There are no more vowels to buy.') # all vowels are gone
    return is_vowel
# option 1 - if user choose 1st option
def option_1(consonants, consonant_used):
    is_consonant = 0 #
    spin = spin_the_wheel()
    if spin != 'BANKRUPT': # landed a number
        print(f'The wheel landed on ${spin:,}.')
        consonant_choice = input(f'Pick a consonant: ')
        while is_consonant == 0:
            is_consonant = choose_consonant(consonant_choice, consonant_used)
            if is_consonant == 0:
                consonant_choice = input(f'Pick a consonant: ')
        consonant_used.append(consonant_choice.upper())
    else: # wheel ended BANKRUPT
        print('The wheel landed on BANKRUPT.')
        consonant_choice = 'NONE'
    return consonant_choice, spin
# option 2 - if user choose 2nd option
def option_2(vowels, earnings, original, used_vowels):
    spending = 0 # money earned starts at zero
    vowels_left = 1
    if (len(used_vowels) != 5): # remaining vowels
        vowel_choice = input('Pick a vowel: ')
        while(choose_vowel(vowel_choice, vowels) == 0) and (vowels_left == 1):
            if len(vowels) == 0:
                vowels_left = 0
            else:
                vowel_choice = input('Pick a vowel: ')
    else:
        print('There are no more vowels to buy.')
        return earnings, 'null', spending, vowels, used_vowels
    # user buys a vowel
    if earnings >= 250:
        earning -= 250
        vowels = get_string(vowels)
        vowels = vowels.replace(vowel_choice.upper(), ' ')
        used_vowels.append(vowel_choice.upper())
        vowels = list(vowels)
        # there's a vowel from a given phrases
        if (vowel_choice.lower() in original) or (vowel_choice.upper() in original):
            count =  (original.count(vowel_choice.lower()) + original.count(vowel_choice.upper()))
            if count == 1:
                print(f'There is 1 {vowel_choice.upper()}.') # one vowel letter
            if count > 1:
                print(f"There are {count} {vowel_choice.upper()}'s.'") # 2+ vowel letter
        else:
            print(f"I'm sorry, there are no {vowel_choice.upper()}'s.'") # no vowel letter
    else: # user does not have money to buy a vowel
        print(f'You need at least $250 to buy a vowel.') # not enought money to buy a vowel
        spending = 1
    return earnings, vowel_choice, spending, vowels, used_vowels
    #return
# possible options and outcomes function
def options(choice, consonants, consonant_used, earnings, original, updated_string, vowels, used_vowels):
    if choice == '1':
        call = option_1(consonants, consonant_used)
        consonant_choice, spin = call[0], call[1]
        if spin != 'BANKRUPT': # wheel spin landed not BANKRUPT
            consonants = get_string(consonants)
            consonants = consonants.replace(consonant_choice.upper(), " ")
            consonants = list(consonants)
            # there's a consonant from a given phrases
            if ((consonant_choice.lower() in original) or (consonant_choice.upper() in original)):
                if ((original.count(consonant_choice.lower()) + original.count(consonant_choice.upper())) == 1):
                    print(f'There is 1 {consonant_choice.upper()}, which earns you ${spin:,}.')
                    earnings += spin
                if ((original.count(consonant_choice.lower()) + original.count(consonant_choice.upper())) > 1):
                    total = (original.count(consonant_choice.lower())) + (original.count(consonant_choice.upper()))
                    spin *= total
                    print(f"There are {total} {consonant_choice.upper()}'s, which earns you ${spin:,}.")
                    earnings += spin
            else:
                print(f"I'm sorry, there are no {consonant_choice.upper()}'s.")
        else: # wheel spin landed BANKRUPT
            print(f'You lost ${earnings:,}!')
            earnings = 0
        updated_string = list(updated_string)
        new_string = get_new_phrase(consonant_choice, original, updated_string)
        updated_string = get_string(updated_string)
        return new_string, earnings, consonants, vowels, used_vowels
    # if user choose option 2
    if choice == '2':
        call = option_2(vowels, earnings, original, used_vowels)
        earnings, vowel_choice, spending, vowels, used_vowels = call[0], call[1], call[2], call[3], call[4]
        if spending == 0:
            updated_string = list(updated_string)
            new_string = get_new_phrase(vowel_choice, original, updated_string)
            updated_string = get_string(updated_string)
            return new_string, earnings, consonants, vowels, used_vowels
        else:
            updated_string = list(updated_string)
            new_string = get_new_phrase('null', original, updated_string)
            updated_string = get_string(updated_string)
            return new_string, earnings, consonants, vowels, used_vowels
# main function
def main():
    # get letter from vowel and consonants functions
    vowels = vowel_list()
    consonants = consonant_list()
    earnings, total_earnings, new_round = 0, 0, 0 # begin round & earnings
    round = 1 # begin round 1
    new_string, used_vowels, consonant_used = [], [], []
    # get phrase from text
    file_stored = get_phrases()
    call = random_phrase(file_stored)
    phrase, original = call[0], call[1]
    # for each letter from given phrase
    for letter in range(len(original)-1):
        if (original[letter] != "'") and (original[letter] != " ") and (original[letter] != '-') and (original[letter] != '&'):
            new_string.append('_')
        else:
            new_string.append(original[letter])
    # get phrases from given text
    phrase = get_string(phrase)
    phrase = str(phrase.replace('\n',''))
    game_display(round, phrase, vowels, consonants, earnings)
    response = user_input()
    while (response != '1') and (response != '2') and (response != '3') and (response != '4'):
        print(f'{response} is an invalid choice.')
        response = user_input()
        # possible combinations from user inputs
    while response != '4' and round <= 4:
        new_round = 0
        # if user choose option 1 or 2
        if response == '1' or response == '2':
            call = options(response, consonants, consonant_used, earnings, original, new_string, vowels, used_vowels)
            new_string, earnings, consonants, vowels, used_vowels = call[0], call[1], call[2], call[3], call[4]
            new_string = get_string(new_string)
            if new_string.upper() != (original.upper()).replace('\n', ''):
                game_display(round, new_string, vowels, consonants, earnings)
                response = user_input()
                # if user choose other than options 1-4
                while (response != '1') and (response != '2') and (response != '3') and (response != '4'):
                    print(f'{response} is an invalid choice.')
                    response = user_input()
            if ((original.upper()).replace('\n', '') == new_string.upper()):
                print('Ladies and gentlemen, we have a winner!')
                print(f'You earned ${earnings:,} this round.')
                new_round = 1
                if earnings < 1000:
                    earnings = 1000
                    total_earnings += earnings
                else:
                    total_earnings += earnings
                    earnings = 0
                round += 1
                vowels = vowel_list()
                consonants = consonant_list()
                new_string, used_vowels, consonant_used = [], [], []
                file_stored = get_phrases()
                call = random_phrase(file_stored)
                phrase, original = call[0], call[0]
            # for every letter from given phrase
                for letter in range(len(original)-1):
                    if (original[letter] != "'") and (original[letter] != ' ') and (original[letter] != '-') and (original[letter] != '&'):
                        new_string.append('_')
                    else:
                        new_string.append(original[letter])
                # get new phrases from given text file
                phrase = get_string(phrase)
                phrase = str(phrase.replace('\n', ''))
                new_string = get_string(new_string)
                if round <= 4:
                    game_display(round, new_string, vowels, consonants, earnings)
                    response = user_input()
                    while (response != '1') and (response != '2') and (response != '3') and (response != '4'):
                        print (f'{response} is an invalid choice.')
                        response = user_input()
                    new_string = list(new_string)
                # if the user does not answer the puzzle correctly
            if ((original.upper()).replace('\n','') == new_string.upper()) and (new_round == 0):
                print("I'm sorry. The correct solution was " + (original.upper()).replace('\n', '') + '.')
                earnings = 0
                print(f'You earned ${earnings:,} this round.')

                new_round = 1
                round += 1
                total_earnings += earnings
                vowels = vowel_list()
                consonants = consonant_list()
                new_string, used_vowels, consonant_used = [], [], []
                file_stored = get_phrases()
                call = random_phrase(file_stored)
                phrase, original = call[0], call[1]

                for letter in range(len(original)-1):
                    if (original[letter] != "'") and (original[letter] != ' ') and (original[letter] != '-') and (original[letter] != '&'):
                        new_string.append('_')
                    else:
                        new_string.append(original[letter])
                phrase = get_string()
                phrase = str(phrase.replace('\n',''))
                new_string = get_string(new_string)
                # if round is at or before #4
                if round <= 4:
                    game_display(round, new_string, vowels, consonants, earnings)
                    response = user_input()
                    while (response != '1') and (response != '2') and (response != '3') and (response != '4'):
                        print(f'{response} is an invalid choice.')
                        response = user_input()
                    new_string = list(new_string)
        # if the user solve the puzzle
        if response == '3' and round <= 4:
            print('Clues: ', end='')
            for letter in range(len(new_string)):
                print(new_string[letter], end='')
            guess = input('\nGuess: ')
            if original.upper().replace('\n', '') == guess.upper():
                new_round = 1
                print('Ladies and gentlemen, we have a winner!')
                if earnings < 1000:
                    earnings = 1000
                    total_earnings += earnings
                else:
                    total_earnings += earnings
                print(f'You earned ${earnings:,} this round.')
                round += 1
                earnings = 0
                vowels = vowel_list()
                consonants = consonant_list()
                new_string, used_vowels, consonant_used = [], [], []
                file_stored = get_phrases()
                call = random_phrase(file_stored)
                phrase, original = call[0], call[1]
                # for every letter from given text file
                for letter in range(len(original)-1):
                    if (original[letter] != "'") and (original[letter] != ' ') and (original[letter] != '-') and (original[letter] != '&'):
                        new_string.append('_')
                    else:
                        new_string.append(original[letter])
                phrase = get_string(phrase)
                phrase = str(phrase.replace('\n', ''))
                new_string = get_string(new_string)
                if round <= 4:
                    game_display(round, new_string, vowels, consonants, earnings)
                    response = user_input()
                    while (response != '1') and (response != '2') and (response != '3') and (response != '4'):
                        print(f'{response} is and invalid choice.')
    # if the user does not solve the puzzle correctly
            if (new_round == 0) and (response == '3') and (round <= 4):
                if guess.upper() != (original.upper()).replace('\n', ''):
                    print("I'm sorry. The correct solution was " + (original.upper()).replace('\n', '') + '.')
                    earnings = 0
                    print(f'You earned ${earnings:,} this round.')
                    new_round = 1
                    round += 1
                    total_earnings += earnings
                    vowels = vowel_list()
                    consonants = consonant_list()
                    new_string, used_vowels, consonant_used = [], [], []
                    file_stored = get_phrases()
                    call = random_phrase(file_stored)
                    phrase, original = call[0], call[1]
                    for letter in range(len(original)-1):
                        if (original[letter] != "'") and (original[letter] != ' ') and (original[letter] != '-') and (original[letter] != '&'):
                            new_string.append('_')
                        else:
                            new_string.append(original[letter])
                    phrase = get_string(phrase)
                    phrase = str(phrase.replace('\n', ''))
                    new_string = get_string(phrase)
                    if round <= 4:
                        game_display(round, new_string, vowels, consonants, earnings)
                        response = user_input()
                        while (response != '1') and (response != '2') and (response != '3') and (response != '4'):
                            print(f'{response} is an invalid choice.')
                            response = user_input()
                                # asks the for user's input again
    # quits the game and returns the total cost
    total_earnings += earnings
    # prints the user's earnings, end round, or quit game
    print(f'You earned ${earnings:,} this round.')
    print(f'Thanks for playing!')
    print(f'You earned a total of ${total_earnings:,}.')


if __name__ == '__main__':
    main()

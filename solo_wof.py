import random as r #Import the random library

'''gameScreen is a function that displays the round, earnings, phrase (with _'s),
   and the available vowels and consonants.'''
def gameScreen(round, phrase, list_vowels, list_consonants, earnings):
    print(f":::::::::::::::::::::::::::::::::::::::::: ROUND {round} of 4 ::") #Display round number
    print("::", phrase.center(52) , "::") #Center the phrase with underscores
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    list_consonants = getString(list_consonants) #Get lists to string form for output purposes
    list_vowels = getString(list_vowels)
    print("::  ", list_consonants.ljust(5), "  ::  ", list_vowels.rjust(5) + "   ::", f"${earnings}".rjust(10), "::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

''' listVowels is a function that is available for resetting the vowel list after
    a round, when called the list list_vowels is populated with all 5 vowels.'''
def listVowels():
    list_vowels = ['A', 'E', 'I', 'O', 'U']
    return list_vowels #Return / Reset list of vowels

''' listConsnants is a function that is available for resetting the consonant list after
    a round, when called the list is populated with all 19 consonants.'''
def listConsonants():
    list_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    return list_consonants #Return / Reset list of consonants

''' getPhrases is a function that reads from 'phrases.txt' and returns the lines as list elements'''
def getPhrases():
    with open('C:/Users/mikew/Desktop/Python/phrases.txt') as fo: #Open file from computer
        file_stored = fo.readlines() #Read file
        fo.close #Close file
    return file_stored #Return file list

''' randomPhrase receives the file_stored list and obtains a random phrase. It also generates the
    random phrases counterpart of underscores, to be updated as the user guesses correct letters.'''
def randomPhrase(file_stored):
    phrase = r.choice(file_stored) #Select random list element
    original_string = phrase #Get a copy before transforming one with underscores
    new_phrase = [] #Initialize new phrase
    copy_phrase = phrase #Get a copy of phrase
    for char in list(copy_phrase): #Traverse the copy of phrase
        new_char = char #Store value of the current character in variable new_char
        if(char.isalpha()): #If it's alphabetic (not ' ', ''', '&', etc), replace with '_'
            new_char = '_'
        new_phrase.append(new_char) #Add new character to list
    return new_phrase, original_string #Return original phrase and underscore counterpart

'''getString is used many times throughout the program, transforming a list into an individual string'''
def getString(list):
    stringForm = "" #Initialize string form
    for i in list: #Traverse the received list
        stringForm += i #Add list character element to newly initialized string
    return stringForm  #Return new string

''' userPrompt is actively displayed throughout the game, and it serves as the control of the users selection.
    as long as the user has not selected 4 and the round has not exceeded 4, this prompt will continue displaying'''
def userPrompt():
    print("What would you like to do?") #4 Options: spin, buy, solve, quit
    print("  1 - Spin the wheel")
    print("  2 - Buy a vowel")
    print("  3 - Solve the puzzle")
    print("  4 - Quit the game")
    users_choice = (input(("Enter the number of your choice: "))) #Get input
    return users_choice #Return input

''' wheelSpin is an imperative function for all cases when users_choice is 1. This is because they spin the
    wheel, determining earnings (or BANKRUPT).'''
def wheelSpin(): #Initialize list first
    spin_list = [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700, 800, 900, 2500, 'BANKRUPT', 'BANKRUPT']
    spin = r.choice(spin_list) #Select a random list element
    return spin #Return this random list element

''' option1 is the function called from calling (control) function when the users_choice is 1. This
    displays what the wheel landed on and screens for a valid consonant input as long as they input
    a single character, a unique consonant (hasn't already been guessed), and not a vowel or special character.'''
def option1(list_consonants, used_consonants):
    isConsonant = 0 #Initialize isConsonant to zero indicating "is it a consonant?" is FALSE
    spin = wheelSpin() #Spin the wheel by calling wheelSpin()
    if(spin != 'BANKRUPT'): #If it's not bankrupt (syntax necessary for adding earnings due to differing data type str for bankrupt)
        print(f"The wheel landed on ${spin}.")
        consonant_choice = input("Pick a consonant: ") #Prompt user for a consonant
        while(isConsonant == 0): #As long as it is not a consonant, continue prompt
            isConsonant = consonantChoice(consonant_choice, used_consonants) #Call consonantChoice for valid input screening
            if(isConsonant == 0): #Screen again
                consonant_choice = input("Pick a consonant: ") #prompt user for a consonant
        used_consonants.append(consonant_choice.upper())
    else: #If the spin IS bankrupt
        print("The wheel landed on BANKRUPT.") #Display to user
        consonant_choice = 'NONE' #There will be no consonant choice for the user at this time
    return consonant_choice, spin #Return consonant choice and spin value that was landed on

''' consonantChoice screens for a valid consonant input from the user '''
def consonantChoice(consonant_choice, used_consonants): #First initialize list of all consonants
    all_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    if(len(consonant_choice) > 1): #If they input more than one character, prompt for only one character
        print("Please enter exactly one character.")
        return 0 #Return false (isConsonant variable in option1 is still FALSE)
    if((consonant_choice.upper() == 'A') or (consonant_choice.upper() == 'E') or (consonant_choice.upper() == 'I') or (consonant_choice.upper() == 'O') or (consonant_choice.upper() == 'U')):
        print("Vowels must be purchased.") #If it's a vowel, indicate as such to user
        return 0 #Return false (isConsonant variable in option1 is still FALSE)
    if((consonant_choice.isalpha()) == 0): #If it is not an alphabetic character ($, &, etc)
        print(f"The character {consonant_choice} is not a letter.") #Indicate this to the user
        return 0 #Return false (isConsonant variable in option1 is still FALSE)
    if(consonant_choice.upper() in used_consonants) and (consonant_choice.upper() in all_consonants):
        print(f"The letter {consonant_choice.upper()} has already been used.")
        return 0 #Return false (isConsonant variable in option1 is still FALSE)
    if((consonant_choice.upper() in all_consonants) and (consonant_choice.upper() not in used_consonants)):
        return 1 #Return false (isConsonant variable in option1 is TRUE)

'''getNewPhrase is called when the underscores must be replaced with the users correctly guessed letters '''
def getNewPhrase(consonant_choice, original, updated_string):
    original = list(original) #Get to list form
    for i in range(len(original)): #Traverse original string
        if((original[i] == consonant_choice) or (original[i] == consonant_choice.upper())): #If it matches original
            updated_string[i] = consonant_choice.upper() #Update with the letter instead of '_'
    return updated_string #Return string with updated letters in place of "_"

''' vowelChoice screens for valid input when users_choice is 2. '''
def vowelChoice(vowel_choice, list_vowels):
    isVowel = 0 #Variable indicating "Is this a vowel?" is initialized to FALSE
    all_vowels = ['A', 'E', 'I', 'O', 'U'] #Initialize lists for all vowels and consonants
    all_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    if (vowel_choice.upper() in all_vowels) and (vowel_choice.upper() in list_vowels): #If it's a vowel:
        isVowel = 1 #listVowel is TRUE
    if vowel_choice.upper() in all_consonants:
        print("Consonants cannot be purchased.") #If in all_consonants, indicate to user
    if(len(vowel_choice) > 1):
        print("Please enter exactly one character.") #If entered more than one character, tell user
    if(vowel_choice.isalpha() == 0): #If not an alpha character
        print(f"The character {vowel_choice} is not a letter.") #Indicate to user (ex. $, %)
    if (vowel_choice.upper() not in list_vowels) and (vowel_choice.isalpha()) and (vowel_choice.upper() in all_vowels):
        print(f"The letter {vowel_choice.upper()} has already been purchased.") #If it's already been used, indicate this to user
    if(len(list_vowels) == 0):
        print("There are no more vowels to buy.") #If the list of vowels is empty, indicate that there are none left
    return isVowel #Return TRUE or FALSE

''' option2 is a function that is called when users_choice is 2.'''
def option2(list_vowels, earnings, original, used_vowels):
    notEnough = 0 #Initialize not enough (representing not enough to buy a vowel) as FALSE
    stillVowels = 1 #Initialze still vowels (representing that there are still vowels left) as TRUE
    if(len(used_vowels) != 5): #If there are still vowels left to buy
        vowel_choice = input("Pick a vowel: ") #Prompt user to pick a vowel
        while (vowelChoice(vowel_choice, list_vowels) == 0) and (stillVowels == 1): #call vowelChoice for valid input
            if(len(list_vowels) == 0): #if the list of vowels is empty:
                stillVowels = 0 #variable representing that there are still vowels is FALSE
            else:
                vowel_choice = input("Pick a vowel: ") #Prompt user if there are still vowels left
    else:
        print("There are no more vowels to buy.") #If used_vowels is of length 5 (full), there are none left
        return earnings, 'null', notEnough, list_vowels, used_vowels #Return null because there's no vowel choice
    if(earnings >= 250): #If they have enough money (at LEAST $250)
        earnings -= 250 #Subtract 250 from their round-earnings
        list_vowels = getString(list_vowels) #convert list_vowels to string
        list_vowels = list_vowels.replace(vowel_choice.upper(), " ") #Replace with blank space
        used_vowels.append(vowel_choice.upper()) #Append choice to used vowels list
        list_vowels = list(list_vowels) #Convert back to a list
        if((vowel_choice.lower() in original) or (vowel_choice.upper() in original)): #If it's in the original string
            count = ((original.count(vowel_choice.lower()) + original.count(vowel_choice.upper())))
            if(count == 1): #Display if there is one of that letter in the string
                print(f"There is one {vowel_choice.upper()}.")
            if(count > 1): #Display if there are more than one of that letter
                print(f"There are {count} {vowel_choice.upper()}'s.'")
        else: #If none present, say 'There are no '_'s'
            print(f"I'm sorry, there are no {vowel_choice.upper()}'s.")
    else: #If not enough, indicate the minimum price to buy a vowel
        print("You need at least $250 to buy a vowel.")
        notEnough = 1 #set not enough -representative variable to TRUE
    return earnings, vowel_choice, notEnough, list_vowels, used_vowels #Return values

''' control is called from option 1 or 2, to control the fx calls to option1 and option 2 when necessary.'''
def control(choice, list_consonants, used_consonants, earnings, original, updated_string, list_vowels, used_vowels):
    if(choice == '1'): #Receive choice -- execute option 1's statements if choice received as 1
        temp = option1(list_consonants, used_consonants) #Call option1 for executing correct statements
        consonant_choice, spin = temp[0], temp[1] #Store return values in variables
        if(spin != 'BANKRUPT'): #If it's not bankrupt (syntax necessary for integer addition/BANKRUPT being a string)
            list_consonants = getString(list_consonants) #convert to string
            list_consonants = list_consonants.replace(consonant_choice.upper(), " ") #Add blank space where necessary
            list_consonants = list(list_consonants) #Convert back to list
            if((consonant_choice.lower() in original) or (consonant_choice.upper() in original)): #If it's present
                if((original.count(consonant_choice.lower()) + original.count(consonant_choice.upper())) == 1):
                    print(f"There is one {consonant_choice.upper()}, which earns you ${spin}.")
                    earnings += spin #Add earnings
                if((original.count(consonant_choice.lower()) + original.count(consonant_choice.upper())) > 1):
                    total = (original.count(consonant_choice.lower())) + (original.count(consonant_choice.upper()))
                    spin = spin * total #Add earnings corresponding to how many of that letter are present
                    print(f"There are {total} {consonant_choice.upper()}'s, which earns you ${spin}.")
                    earnings += spin #Add earnings
            else: #If not present, indicate to the user that there are none of that letter.
                print(f"I'm sorry, there are no {consonant_choice.upper()}'s.")
        else: #If it IS BANKRUPT, indicate how much they lost.
            print(f'You lost ${earnings}!')
            earnings = 0 #Set earnings to zero
        updated_string = list(updated_string) #get updated_string to a list
        new_string = getNewPhrase(consonant_choice, original, updated_string) #replace phrase with appropriate letters
        updated_string = getString(updated_string) #get updated_string back to a string
        return new_string, earnings, list_consonants, list_vowels, used_vowels #Return values
    if(choice == '2'): #If choice is 2
        temp = option2(list_vowels, earnings, original, used_vowels) #Call option2 for correct exec statements
        earnings, vowel_choice, notEnough, list_vowels, used_vowels = temp[0], temp[1], temp[2], temp[3], temp[4]
        if(notEnough == 0): #If they DO have enough for a vowel
            updated_string = list(updated_string) #Convert updated_string to a list
            new_string = getNewPhrase(vowel_choice, original, updated_string) #get updated string
            updated_string = getString(updated_string) #Convert back to a string
            return new_string, earnings, list_consonants, list_vowels, used_vowels #Return values
        else: #If they DONT have enough for a vowel
            updated_string = list(updated_string) #Convert updated_string to a list
            new_string = getNewPhrase('null', original, updated_string) #New string will have no changes
            updated_string = getString(updated_string) #Get back to string and uphold consistent return statements
            return new_string, earnings, list_consonants, list_vowels, used_vowels

''' main -- this function initializes necessary lists and variables. It calls control and serves as the
    headquarters of this WOF game. It continues executing a lengthy block of code as long as option is
    not equal to 4 and the round has not exceeded 4.'''
def main():
#Initialize values for first display
  list_vowels = listVowels() #Initialize lists of vowels and consonants
  list_consonants = listConsonants()
  earnings = 0 #Initialize earnings
  total_earnings = 0
  round = 1 #Initialize rounds and if a newRound is in effect
  newRound = 0
  new_string, used_vowels = [], [] #Initialize lists for the new string and for used vowels
  used_consonants = [] #Initialize list for used consonants
  file_stored = getPhrases() #get file_stored from getPhrases function
  temp = randomPhrase(file_stored) #Get return values (one original, one with _'s)
  phrase, original = temp[0], temp[1] #store in phrase and original variables
  for i in range(len(original) - 1): #Traverse original string
      if((original[i] != "'") and (original[i] != ' ') and (original[i] != '-') and (original[i] != '&')):
          new_string.append('_') #Add _ where necessary for new_string with _'s
      else:
          new_string.append(original[i]) #If it's a non-alpha char, append it to new_string as is
  phrase = getString(phrase) #Get in string form
  phrase = str(phrase.replace("\n", "")) #Replace \n for consistency/formatting
  gameScreen(round, phrase, list_vowels, list_consonants, earnings) #Display game screen to user
  users_choice = userPrompt() #Prompt user
  while((users_choice != '1') and (users_choice != '2') and (users_choice != '3') and (users_choice != '4')):
      print(f"{users_choice} is an invalid choice.") #If their choice is invalid, indicate so
      users_choice = userPrompt() #Prompt user
  while((users_choice != '4') and (round <= 4)):
      newRound = 0
      if(users_choice == '1') or (users_choice == '2'):
        temp = control(users_choice, list_consonants, used_consonants, earnings, original, new_string, list_vowels, used_vowels)
        new_string, earnings, list_consonants, list_vowels, used_vowels = temp[0], temp[1], temp[2], temp[3], temp[4]
        new_string = getString(new_string)
        if(new_string.upper() != (original.upper()).replace("\n", "")):
          gameScreen(round, new_string, list_vowels, list_consonants, earnings)
          users_choice = userPrompt()
          while((users_choice != '1') and (users_choice != '2') and (users_choice != '3') and (users_choice != '4')):
              print(f"{users_choice} is an invalid choice.")
              users_choice = userPrompt()
        #print("New String: ", new_string.upper(), "\nOriginal: ", original.upper())
        if((original.upper()).replace("\n", "") == new_string.upper()):
          print("Ladies and gentlemen, we have a winner!")
          print(f"You earned ${earnings} this round.")
          newRound = 1
          if(earnings < 1000):
              total_earnings += 1000
              earnings = 0
          else:
              total_earnings += earnings
              earnings = 0
          round = round + 1
          list_vowels = listVowels()
          list_consonants = listConsonants()
          new_string, used_vowels = [], []
          used_consonants = []
          file_stored = getPhrases()
          temp = randomPhrase(file_stored)
          phrase, original = temp[0], temp[1]
          #print("Phrase: ", phrase, "\nOriginal: ", original)
          for i in range(len(original) - 1):
              if((original[i] != "'") and (original[i] != ' ') and (original[i] != '-') and (original[i] != '&')):
                  new_string.append('_')
              else:
                  new_string.append(original[i])
          phrase = getString(phrase)
          phrase = str(phrase.replace("\n", ""))
          new_string = getString(new_string)
          if(round <= 4):
              gameScreen(round, new_string, list_vowels, list_consonants, earnings)
              users_choice = userPrompt()
              while((users_choice != '1') and (users_choice != '2') and (users_choice != '3') and (users_choice != '4')):
                  print(f"{users_choice} is an invalid choice.")
                  users_choice = userPrompt()
              new_string = list(new_string)
        if((original.upper()).replace("\n", "") == new_string.upper()) and (newRound == 0):
            print("I'm sorry. The correct solution was "+ (original.upper()).replace("\n", "") + ".")
            earnings = 0
            print(f"You earned ${earnings} this round.")
            newRound = 1
            round = round + 1
            total_earnings += earnings
            list_vowels = listVowels()
            list_consonants = listConsonants()
            new_string, used_vowels = [], []
            used_consonants = []
            file_stored = getPhrases()
            temp = randomPhrase(file_stored)
            phrase, original = temp[0], temp[1]
            #print("Phrase: ", phrase, "\nOriginal: ", original)
            for i in range(len(original) - 1):
                if((original[i] != "'") and (original[i] != ' ') and (original[i] != '-') and (original[i] != '&')):
                    new_string.append('_')
                else:
                    new_string.append(original[i])
            phrase = getString(phrase)
            phrase = str(phrase.replace("\n", ""))
            new_string = getString(new_string)
            if(round <= 4):
                gameScreen(round, new_string, list_vowels, list_consonants, earnings)
                users_choice = userPrompt()
                while((users_choice != '1') and (users_choice != '2') and (users_choice != '3') and (users_choice != '4')):
                    print(f"{users_choice} is an invalid choice.")
                    users_choice = userPrompt()
      if(users_choice == '3') and (round <= 4):
              print("Clues: ", end = '')
              for i in range(len(new_string)):
                  print(new_string[i], end = '')
              guess = input("\nGuess: ")
              if((original.upper()).replace("\n", "") == guess.upper()):
                  newRound = 1
                  print("Ladies and gentlemen, we have a winner!")
                  if(earnings < 1000):
                      earnings = 1000
                      total_earnings += earnings
                  else:
                      total_earnings += earnings
                  print(f"You earned ${earnings} this round.")
                  round = round + 1
                  earnings = 0
                  list_vowels = listVowels()
                  list_consonants = listConsonants()
                  new_string, used_vowels = [], []
                  used_consonants = []
                  file_stored = getPhrases()
                  temp = randomPhrase(file_stored)
                  phrase, original = temp[0], temp[1]
                  #print("Phrase: ", phrase, "\nOriginal: ", original)
                  for i in range(len(original) - 1):
                      if((original[i] != "'") and (original[i] != ' ') and (original[i] != '-') and (original[i] != '&')):
                          new_string.append('_')
                      else:
                          new_string.append(original[i])
                  phrase = getString(phrase)
                  phrase = str(phrase.replace("\n", ""))
                  new_string = getString(new_string)
                  if(round <= 4):
                      gameScreen(round, new_string, list_vowels, list_consonants, earnings)
                      users_choice = userPrompt()
                      while((users_choice != '1') and (users_choice != '2') and (users_choice != '3') and (users_choice != '4')):
                          print(f"{users_choice} is an invalid choice.")

              if((newRound == 0) and (users_choice == '3')) and (round <= 4):
                  if(guess.upper() != (original.upper()).replace("\n", "")):
                      print("I'm sorry. The correct solution was "+ (original.upper()).replace("\n", "") + ".")
                      earnings = 0
                      print(f"You earned ${earnings} this round.")
                      newRound = 1
                      round = round + 1
                      total_earnings += earnings
                      list_vowels = listVowels()
                      list_consonants = listConsonants()
                      new_string, used_vowels = [], []
                      used_consonants = []
                      file_stored = getPhrases()
                      temp = randomPhrase(file_stored)
                      phrase, original = temp[0], temp[1]
                      #print("Phrase: ", phrase, "\nOriginal: ", original)
                      for i in range(len(original) - 1):
                          if((original[i] != "'") and (original[i] != ' ') and (original[i] != '-') and (original[i] != '&')):
                              new_string.append('_')
                          else:
                              new_string.append(original[i])
                      phrase = getString(phrase)
                      phrase = str(phrase.replace("\n", ""))
                      new_string = getString(new_string)
                      if(round <= 4):
                          gameScreen(round, new_string, list_vowels, list_consonants, earnings)
                          users_choice = userPrompt()
                          while((users_choice != '1') and (users_choice != '2') and (users_choice != '3') and (users_choice != '4')):
                              print(f"{users_choice} is an invalid choice.")
                              users_choice = userPrompt()
      #new_string = getString(new_string)
      #print("New String UPPER: ", new_string.upper(), "\nOriginal: ", original.upper())

      #if((original.upper()).replace("\n", "") == new_string.upper()):
        #print("Ladies and gentlemen, we have a winner!")
        #print(f"You earned ${earnings} this round.")
        #earnings = 0
        #round = round + 1
      #new_string = list(new_string)
  total_earnings += earnings
  print(f"Thanks for playing! \nYou earned a total of ${total_earnings}.")
main()


main.py:

import random
import re

class Wheel_Of_Fortune:
    def __init__(self):
        self.consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'Y']
        self.vowels = ['A', 'E', 'I', 'O', 'U']
        self.money = 0
        self.phrase = ""
        self.round = 0
        self.wheel = (500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700, 800, 900, 2500, "BANKRUPT", "BANKRUPT")
        self.discoveredLetters = []

    def choosePhrase(self):
        phrases_file = open("phrases.txt")
        phrases = (phrases_file.read()).split("\n")
        self.phrase = random.choice(phrases)
        self.phrase = self.phrase.upper()

    def displayMenu(self):
        if (self.round < 4 or self.round == 4) and (len(self.discoveredLetters) == 0):
            self.round += 1
            print (":" * 42, "ROUND ", self.round, " of 4 ", ":" * 2)
            print (":" * 2, " " * 6, end=" ")
            pattern = "/^[A-Za-z]+$/"
            for i in self.phrase:
                result = re.match(pattern, i)
                if i == " ":
                    print (i, end = " ")

                elif result:
                    print (i, end = " ")

                else:
                    print ("_", end = " ")

            print (" " * 6, ":" * 2)

            print (":" * 2, " " * 3, end="")
            for i in self.consonants:
                print (i, end="")
            print (" " * 3, ":" * 2, " " * 3, end="")
            for i in self.vowels:
                print (i, end = "")

            print (" " * 6, ":" * 2, " " * 2, "$", self.money, ":" * 2)
            print (":" * 61)

            return True

        elif len(self.discoveredLetters) > 0 and self.round < 4:
            self.round += 1
            print (":" * 42, "ROUND ", self.round, " of 4 ", ":" * 2)
            print (":" * 2, " " * 6, end=" ")
            pattern = "/^[A-Za-z]+$/"
            for i in self.phrase:
                result = re.match(pattern, i)
                if i == " ":
                    print (i, end = " ")

                elif i.upper() in self.discoveredLetters:
                    print (i.upper(), end=" ")

                elif result:
                    print (i, end = " ")

                else:
                    print ("_", end = " ")

            print (" " * 6, ":" * 2)

            print (":" * 2, " " * 3, end="")
            for i in self.consonants:
                print (i, end="")
            print (" " * 3, ":" * 2, " " * 3, end="")
            for i in self.vowels:
                print (i, end = "")

            print (" " * 6, ":" * 2, " " * 2, "$", self.money, ":" * 2)
            print (":" * 61)

            return True

        else:
            return False

    def spinTheWheel(self):
        choice = random.choice(self.wheel)
        if (choice == "BANKRUPT"):
            self.money = 0
            return choice

        else:
            self.money += choice
            return self.money

    def entered_choice(self, letter):
        if (letter.upper() in self.phrase) and (letter.upper() in self.consonants):
            print ("There are ", self.phrase.count(letter.upper()), ", which earns you $", self.phrase.count(letter.upper()) * self.money)
            self.money = self.phrase.count(letter.upper()) * self.money
            self.discoveredLetters.append(letter.upper())
            self.consonants.remove(letter.upper())

        else:
            print ("I'm sorry, there are no ", letter.upper(), "'s.")
            self.consonants.remove(letter.upper())
            if (self.money > 0):
                self.money = self.money

            else:
                self.money = 0

    def buyVowel(self, vowel_choice):
        if (self.money > 250) and (vowel_choice.upper() not in self.consonants) and (vowel_choice.upper() in self.vowels):
            self.money -= 250
            print ("Your purchase has been made successfully!!")
            self.discoveredLetters.append(vowel_choice.upper())
            self.vowels.remove(vowel_choice.upper())

        else:
            print ("Sorry, either you do not have enough money to buy a vowel or you haven't entered a vowel or you haeve already guessed that vowel!!")
            self.vowels.remove(vowel_choice.upper())


if __name__ == "__main__":
    wof = Wheel_Of_Fortune()
    wof.choosePhrase()

    while (wof.displayMenu()):

        print ("What would you like to do?")
        print (" " * 2, "1 - Spin the wheel")
        print (" " * 2, "2 - Buy a vowel")
        print (" " * 2, "3 - Solve the puzzle")
        print (" " * 2, "4 - Quit the game")
        print ("Enter the number of your choice: ", end = "")
        choice = int(input ())

        if (choice == 1):
            wheel_value = wof.spinTheWheel()
            print ("The wheel landed on $", wheel_value)
            if (wheel_value == "BANKRUPT"):
                print ("OOPS, you're BANKRUPT!!")
            else:
                while (True):
                    print ("Pick a consonant: ", end = "")
                    consonant_choice = input()
                    if consonant_choice.upper() in wof.vowels:
                        print ("Vowels must be purchased")
                    elif len(consonant_choice) > 1:
                        print ("Please enter exactly one character")
                    else:
                        try:
                            int (consonant_choice)
                            print (consonant_choice, " is not a letter")
                        except:
                            wof.entered_choice(consonant_choice)
                            break

        elif (choice == 2):
            print ("Enter vowel from available vowels to buy: ", end = "")
            vowel_choice = input()
            wof.buyVowel(vowel_choice)

        elif (choice == 3):
            print ("Enter the phrase: ", end="")
            phrase_entered = input()
            if (wof.phrase.upper() == phrase_entered.upper()):
                print ("You have won the game!!")
                if (wof.money > 1000):
                    print ("You have won $", wof.money)
                    break
                else:
                    print ("You have won $", 1000)
                    break

            else:
                print ("Your guess was incorrect")

        elif (choice == 4):
            break

        else:
            print ("Wrong Choice!! Try Again!!")

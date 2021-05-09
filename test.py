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

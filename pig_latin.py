################################################################################
# Description: Programs to get the user's sentence and returns into Pig Latin
# sentence or word(s)
################################################################################

def main():
    # input a string from user
    sentence = input("Enter a string: ")
    #words = string.split(' ')
    new_sentence = pig(sentence)

    # print new string in pig latin
    print(new_sentence)
    #new_sentence = pig(string)
    #print(new_sentence)

#def convert_word(word):
#    first_letter = word[0]
#    return word[1:] + word[0] + "ay"

# Pig Latin function
def pig(sentence):
    words = sentence.split(' ')
    new_words = []
    #list_of_words = string.split()
    #new_sentence = ""
    #pig_latin = ""

    for word in words:
        if word[-1].isalpha():
            new_words.append(word[1:] + word[0] + 'ay')
        else:
            new_words.append(word[1:-1] + word[0] + 'ay' + word[-1])

    new_sentence = ' '.join(new_words)
    # iterate each word
    #for word in list_of_words:
        # convert to pig latin and create a new sentence
        #new_sentence = new_sentence + convert_word(word)
        #pig_latin = pig_latin + (word[1:] + word[0] + "ay")

    return new_sentence.capitalize()
    #return pig_latin.capitalize()

if __name__ == '__main__':
    main()

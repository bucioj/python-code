###############################################################################
# This program implements a madlibs game
###############################################################################

def get_valid_word(speech):
    '''function to make sure the user does not enter a blank word'''
    while True:
        word = input(f'Enter a/an {speech}: ')
        # check to make sure the user entered some text
        if word != "":
            return word
        else:
            # if no text was entered, display an error message
            print('  ERROR: Please enter a word')

def main():
    # initialize the story template
    template = "A vacation is when you take a trip to some _ place with your _ family. Usually you go to some place that's near a/an _ or up on a/an _."

    # split the template string into a list of words; words are separated by spaces
    template_list = template.split(" ")

    # find which words contain blanks ("_" character)
    blank_indices = []
    for i in range(len(template_list)):
        if '_' in template_list[i]:
            # when a blank is found, record its index
            blank_indices.append(i)

    # initialize parts of speech for each blank in order
    parts_of_speech = ['adjective','adjective','noun','noun']

    # zip together blank indicies and parts of speech
    # in other words: make tuples where the index of a blank corresponds to its part of speech
    blanks = zip(blank_indices, parts_of_speech)

    # get user input for each blank
    for position, speech in blanks: # position = index of blank, speech = corresponding part of speech
        word = get_valid_word(speech)
        template_list[pos] = template_list[pos].replace('_', word)

    # display full story
    print(' '.join(template_list)) # join does opposite of split

if __name__ == '__main__':
    main()

################################################################################
# Author: Jose Bucio
# Date: 04/05/2021
# Description: Programs that processes given two text files and produce the following
# outputs by printed one per line in alphabetical order and correct formated colon, space, and number of times
################################################################################
import string

def main():
    # named dictionary 1 and 2 from xian text files
    dict_1 = get_dictionary('xian_1.txt')
    dict_2 = get_dictionary('xian_2.txt')

    # write the dictionary file for xian 1 & 2
    write_dict_file('xian_1_word_frequency.txt', dict_1)
    write_dict_file('xian_2_word_frequency.txt', dict_2)

    # declare words 1 & 2 for each set of keys from dictionary
    words_1 = set(dict_1.keys())
    words_2 = set(dict_2.keys())

    # comparison using intersection and sysmmetric_difference
    # create files to determine common words and non common words from xian files
    write_list_file('common_words.txt', words_1.intersection(words_2))
    write_list_file('eitherbutnotboth.txt', words_1.symmetric_difference(words_2))

# create dictionary function
def get_dictionary(file_name):
    # create dictionary named frequency
    frequency = {}
    with open(file_name) as foo:
        # for every line given from file
        for line in foo:
            words = line.split()
            words = [word.strip(string.punctuation).lower() for word in words]
            # for very words in words dict
            for word in words:
                # keeps track of the words from file
                frequency[word] = frequency.get(word,0) + 1
    return frequency # returns the numbers of words found

# write dictionary file function
def write_dict_file(file_name, frequency):
    with open(file_name, 'w') as foo:
        # sorted the words
        for key in sorted(frequency.keys()):
            # writes the correct format
            #foo.write(f'{key:s} {frequency[key]:d}\n')
            foo.write("{:s}: {:d}\n".format(key,frequency[key]))

# write list file function
def write_list_file(file_name, words):
    with open(file_name, 'w') as foo:
        # for every word from sorted words
        for word in sorted(words):
            # write the correct format
            foo.write("{:s}\n".format(word))

if __name__ == '__main__':
    main()

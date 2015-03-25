#!/usr/bin/python
import urllib.request
from os.path import dirname


global dictionary


# Creates a Dictionary from given text
def dict_parser(text_file):
    with open(text_file) as txt:
        global dictionary
        dictionary = txt.read().splitlines()
    return dictionary


# Uses Binary Search Methods to locate user word
def is_word_in_dict(dictionary, word, left=0):
        right = len(dictionary)-1
        while right >= left:
            middle = (left+right)//2
            if dictionary[middle] == word:
                return True
            elif dictionary[middle] < word:
                left = middle+1
            elif dictionary[middle] > word:
                right = middle - 1
            elif left > right:
                print(word)
            else:
                return False


def main():
    # Readability purposes
    divider = '------------------------------------------------------------'
    print(divider)
    print('             Welcome to PySpellCheck 2.0a                 ')
    print(divider + '\n')

    print(divider)
    dict_version = input('Would you like a ONLINE or OFFLINE Dictionary? ').lower()
    # Checks for non-valid keywords
    while dict_version != "offline" and dict_version != "online":
        dict_version = input('ONLINE or OFFLINE Dictionary? ').lower()

    if dict_version == "offline":
        parent_direct = dirname(dirname(__file__))
        dict_lang = parent_direct + '/dict_locale/' + input('Select your language locale ') + ".txt"
        global dictionary
        dictionary = dict_parser(dict_lang)
    else:
        # Creates Dictionary from URL
        url = "http://goo.gl/dz2H3E"
        online_dict = urllib.request.urlopen(url)
        dictionary = online_dict.read().splitlines()

    user_continue = True
    while user_continue :
        word = input("Give me a word to Spell Check! ").lower()
        while not word.isalpha():
            word = input("Give me a WORD to Spell Check! ").lower()
        print(divider + '\n')

        if is_word_in_dict(dictionary, word):
            print("The Word, " + word + ", is spelled correctly!")
        else:
            print("The Word, " + word + ", is NOT spelled correctly!")

        contin_check = input("\nWould you like to use the checker again? ").lower()
        if contin_check != 'yes':
            user_continue = False

# Calls Main Program
if __name__ == '__main__':
    main()

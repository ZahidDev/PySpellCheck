#!/usr/bin/python
import urllib.request

#Creates a Dictionary from given text
def parser(text_file):
    with open(text_file) as txt:
        dictionary = txt.read().splitlines()
    return dictionary


def main():
    #Readability purposes
    divider = '------------------------------------------------------------'
    print(divider)
    print('             Welcome to PySpellCheck Pre-Alpha                  ')
    print(divider + '\n')

    print(divider)
    dictver = input('Would you like a ONLINE or OFFLINE Dictionary? ').lower()
    #Checks for non-valid keywords
    while dictver != "offline" and dictver != "online":
        dictver = input('ONLINE or OFFLINE Dictionary? ').lower()

    if dictver == "offline":
        text_file = input('Give me the name of the Dictionary! ') + ".txt"
        dictionary = parser(text_file)
    else:
        #Creates Dictionary from URL
        url = "http://goo.gl/dz2H3E"
        onl_dict = urllib.request.urlopen(url)
        dictionary = onl_dict.read().splitlines()

    contin = True
    while contin == True:
        word = input("Give me a word to Spell Check! ").lower()
        while not word.isalpha():
            word = input("Give me a word to Spell Check! ").lower()
        print(divider + '\n')

        #Uses Binary Search Methods to locate user word
        def isWordinDictionary(word, left=0, right=len(dictionary)-1):
            if dictver == "online":
            	#Turns str to bytes
                word = word.encode('utf-8')
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

        if isWordinDictionary(word):
            print("The Word, " + word + ", is spelled correctly!")
        else:
            print("The Word, " + word + ", is NOT spelled correctly!")

        contin_check = input("\nWould you like to use the checker again? ").lower()
        if contin_check != 'yes':
            contin = False

#Calls Main Program
if __name__ == '__main__':
    main()

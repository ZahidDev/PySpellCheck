from os.path import dirname
import re
import requests.exceptions


class Dictionary(object):
    def __init__(self):
        self.dictionary = []

    def offline_dict_parser(self, text_file):
        """
        Reads Locale Dictionary files and returns a OFFLINE
        dictionary.

        :param text_file: takes a user inputed dictionary local list
        :return: A dictionary list
        """

        with open(text_file) as txt:
            self.dictionary = txt.read().splitlines()
        return self.dictionary

    def get_dictionary(self):
        """
        Uses user input to pre-load specific dictionary for spell
        checking use.

        :return: void
        """

        dict_version = input('Would you like a ONLINE or OFFLINE Dictionary? ').lower()
        # Checks for non-valid keywords
        while dict_version != "offline" and dict_version != "online":
            dict_version = input('ONLINE or OFFLINE Dictionary? ').lower()

        if dict_version == "offline":
            # Locates directory for locale files
            parent_direct = dirname(dirname(__file__))
            dict_lang = parent_direct + '/dict_locale/' + input('Select your language locale ') + ".txt"
            self.dictionary = self.offline_dict_parser(dict_lang)
        else:
            # Creates Dictionary from URL
            online_dicts = {"EN": "http://goo.gl/dz2H3E"}
            dict_lang = input('Select your language locale |EN| ').upper()
            try:
                get_online_dict = requests.get(online_dicts[dict_lang])
                self.dictionary = get_online_dict.text.splitlines()
            except requests.exceptions.ConnectionError:
                print("Cannot connect to the internet. Please check your connection/firewall settings.")
                exit()

    def is_word_in_dict(self, word):
        """
        Uses Binary Search (for now) to locate if user input value
        is correctly spelled if found in list.

        :param word: user input word(string) value.
        :return: bool
        """

        left = 0
        dictionary = self.dictionary
        right = len(dictionary) - 1
        while right >= left:
            middle = (left + right) // 2
            if dictionary[middle] == word:
                return True
            elif dictionary[middle] < word:
                left = middle + 1
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
    print('             Welcome to PySpellCheck 2.5b                 ')
    print(divider + '\n')

    print(divider)

    py_dictionary = Dictionary()
    py_dictionary.get_dictionary()

    user_continue = True
    while user_continue:
        user_text = input("Give me some text to Spell Check! ").lower()
        # Removes punctuation from spell checking
        text_list = re.findall(r'\w+', user_text)

        for word in text_list:
            if not word.isalpha() or word == 'i':
                text_list.remove(word)

        no_errors = True
        for word in text_list:
            if not py_dictionary.is_word_in_dict(word):
                no_errors = False
                print("\n" + divider)
                print("The Word, " + word + ", is NOT spelled correctly!")
                print(divider)

        if no_errors:
            print("\nNo spelling errors were found!")

        contin_check = input("\nWould you like to use the checker again? ").lower()
        if contin_check != 'yes':
            user_continue = False

# Calls Main Program
if __name__ == '__main__':
    main()

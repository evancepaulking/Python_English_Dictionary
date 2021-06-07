# English Dictionary  using python
# ------------------------------------------
# import required libraries

import json
from difflib import get_close_matches

# load json file containing key value
dict_data = json.load(open("english_dic_data.json"))

# input from user:
while True:
    user_word = input('Enter word you want it\'s meaning: ')


    def word_fetch(user_data):
        # allow any form of input, capital letter, small letter or title.
        word = user_word.lower()
        if word in dict_data:
            # checking if the word has more than one meaning
            mult_meaning = dict_data[word]
            if len(mult_meaning) > 1:

                for i in mult_meaning :
                    print(i)
            else:
                print(dict_data[word][0])

        # get a closer match
        elif (len(get_close_matches(word, dict_data.keys(),3))) > 0:
            closer_match = get_close_matches(word, dict_data.keys())[0]
            print("Did you mean {} instead? Enter Y if 'Yes' or N if 'no': ".format(closer_match))

            # selections for yes or no
            selection = input().lower()
            if selection == 'y':
                return closer_match
            elif selection == 'n':
                print('Sorry, this word can\'t be found in our dictionary, please check the spelling again')
            else:
                print("We didn't understand your entry, sorry!!")
        else:
            print("The word doesn't exist. Please double check it")


    if __name__ == '__main__':
        word_fetch(user_word)
        print()
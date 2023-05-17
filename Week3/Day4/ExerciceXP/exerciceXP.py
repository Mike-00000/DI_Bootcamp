
# EXERCICES XP ------------------------------------------------------
# Exercise 1 – Random Sentence Generator-----------------------------
def get_words_from_file():
    huge_list = []
    with open("wordlist.txt", "r") as f:
        for line in f:
            huge_list.extend(line.split())
            # print(huge_list)
    return huge_list


import string
import random
def get_random_sentence(lenght):
    words_list = get_words_from_file()
    randon_string = ' '.join(random.choices(words_list, k=lenght))
    print(randon_string)
    return randon_string

get_random_sentence(7)


lowercased_words = get_random_sentence(7)
print(lowercased_words.lower())



def main():
    print("This program is about to print a message and ask you how long you want the sentence to be, and check if you inputed correct or incorrect data ")
    sentence_lenght = int(input("how long you want the sentence to be (acceptable values are: an integer between 2 and 20)? "))
    try:
        if type(sentence_lenght) != int:
            raise TypeError("Error! Not an integer")
        if sentence_lenght < 2 or sentence_lenght > 20:
            raise ValueError("Error! integer not between 2 and 20")
    except TypeError as error1 :
        print("TYPE ERROR")
        print(error1)
    except ValueError as error2 :
        print("VALUE ERROR")
        print("error2")
    else:
        get_random_sentence(sentence_lenght)

main()

# Exercise 2: Working With JSON -------------------------------------

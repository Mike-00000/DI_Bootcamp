

# Exercise 3 : Outputs
# Instructions
# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9 TRUE
#     >>> 3 == 3 == 3 TRUE
#     >>> bool(0) -> FALSE
#     >>> bool(5 == "5") FALSE
#     >>> bool(4 == 4) == bool("4" == "4") TRUE (but I said first FALSE)
#     >>> bool(bool(None)) FALSE (but I did'n know)

    # x = (1 == True) 
    # y = (1 == False) 
    # a = True + 4 
    # b = False + 10 
    # print("x is", x)
    # print("y is", y)
    # print("a:", a)
    # print("b:", b)

# ----------------------------------------
# Exercise 4 : How Many Characters In A Sentence ?
# Instructions
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))


# ----------------------------------------
# Exercise 5: Longest Word Without A Specific Character
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.
sentence = input("input the longest sentence you can without the character “A” ")
if "a" in sentence:
    print("There is an 'a' in your sentence; you lost!")
else:
    print("Good job; there is no 'a' in your sentence. It's length is " + str(len(sentence)) + " caracteres")
    print("Can you do better?")
    sentence2 = input("input the longest sentence you can without the character “A” ")
    if "a" in sentence2:
        print("There is an 'a' in your sentence; you lost!")
    else:
        if len(sentence2) > len(sentence):
            print("Good job! Its longer than the previous one. It's length is " + str(len(sentence2)) + " caracteres.  You're the best!")
        else:
            print("Bad job! It's length is " + str(len(sentence2)) + " caracteres. Its not longer than the previous one. You lose!")
            
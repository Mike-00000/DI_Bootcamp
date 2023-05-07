# Exercise 1 : Hello World-I Love Python
# Print the following output in one line of code:
print("Hello World "*4 + "I love python "*4)


# Exercise 2 : What Is The Season ?
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)
season = int(input("Input a month (1 to 12)"))
if 1 <= season <= 2:
    print("It's winter")
elif season == 12:
    print("It's winter")
elif 3 <= season < 6:
    print("It's spring")
elif 6 <= season < 9:
    print("It's summer")
elif 9 <= season < 12:
    print("It's autumn")
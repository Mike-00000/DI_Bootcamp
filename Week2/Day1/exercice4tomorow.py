# Here is a table of prices for a wedding catering company:

# # of guests	price
# Up to 50 people	$4,000
# Up to 100 people	$10,000
# Up to 200 people	$15,000
# More than 200 people	$20,000

# 📝 Instructions:

# Please write an program that prompts the user for the number of people attending their wedding and prints the corresponding price in the console.
# For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.



nbre_people = int(input("How many people is attending?" ))

if 1 <= nbre_people <= 50:
    print("It will cost $4000")
elif 51 <= nbre_people <= 100:
    print("It will cost $10000")
elif 101 <= nbre_people <= 200:
    print("It will cost $15000")
else :
    print("It will cost $20000")



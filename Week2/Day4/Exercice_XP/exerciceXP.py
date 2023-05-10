

# Exercice XP ---------------------------------------------------------------------------------
# Exercie 1 - What Are You Learning ? ---------------------------------------------------------
# def display_message():
#     print("Hi, I'm learning Python")
# display_message()




# Exercie 2 - What’s Your Favorite Book ? ------------------------------------------------------
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
# favorite_book("Ubik")




# Exercie 3 - Some Geography -------------------------------------------------------------------
# def describe_city(city, country="Unknown"):
#     print(f"{city} is in {country}")
# describe_city("Paris", "France")




# Exercise 4 : Random ----------------------------------------------------------------------------
# from random import randint
# def rand_number():
#     random_input = int(input("Give me a number enter 1 and 100 "))
#     random_number = randint(1, 100)
#     if random_input == rand_number:
#         print("Great! You found it! ")
#     else:
#         print(f"You lose! You choose {random_input} but the good one was {random_number}! ")

# rand_number()




# Exercise 5 : Let’s Create Some Personalized Shirts ! ------------------------------------------------
# Version 1 ---------------------------------
# def making_shirt():
#     your_size = input("What is your size? ")
#     your_text = input("What is your text? ")
#     print(f"Your size is {your_size} and your text is '{your_text}'")
# making_shirt()
# -------------------------------------------

# Version 2 ---------------------------------
# def make_shirt(size="L", text="I love Python"):
#     print(f"The size is {size} and the text is '{text}'")
# make_shirt()
# make_shirt("L")
# make_shirt("M")
# make_shirt("S", "I only love myself!")
# make_shirt(size="M", text="I want to eat")




# Exercise 6 : Magicians … -------------------------------------------------------------------------------
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians():
#     for i in magician_names:
#         print(i)
# show_magicians()

# def make_great():
#     for i in range(len(magician_names)):
#         magician_names[i] = magician_names[i] + " The Great"
#     print(magician_names)
# make_great()
# show_magicians()




# Exercise 7 : Temperature Advice ---------------------------------------------------------------------------
#  Part 1 to 3 : -----------------------------------
from random import randint
# def get_random_temp():
#     rand_temp = randint(-10, 40)
#     return rand_temp

# def main():
#     temp = get_random_temp()
#     if temp < 0 :
#         print(f"The temperature right now is {temp} degrees Celsius. Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= temp < 16:
#         print(f"The temperature right now is {temp} degrees Celsius. Quite chilly! Don’t forget your coat")
#     elif 16 <= temp <= 23:
#         print(f"The temperature right now is {temp} degrees Celsius. Not bad")
#     elif 24 <= temp < 32:
#         print(f"The temperature right now is {temp} degrees Celsius. That's great! It's hot! Time to swimming pool")
#     elif 32 <= temp < 40:
#         print(f"The temperature right now is {temp} degrees Celsius. Be carful!!! It's very hot!!! Stay at home and drink a lot")
#     else:
#         print(f"The temperature right now is {temp} degrees Celsius. Prepare to die!")
# main()

#  Part 4 : -----------------------------------------
def get_random_temp2(season):
    
    if season == "winter":
        temp = randint(-10, 5)
        print(f"The temperature right now is {temp} degrees Celsius. Brrr, that’s freezing! Wear some extra layers today")
    elif season == "spring":
        temp = randint(6, 23)
        print(f"The temperature right now is {temp} degrees Celsius. Not bad")
    elif season == "summer":
        temp = randint(24, 35)
        print(f"The temperature right now is {temp} degrees Celsius. That's great! It's hot! Time to swimming pool")
    elif season == "autumn":
        temp = randint(6, 23)
        print(f"The temperature right now is {temp} degrees Celsius. Not bad")
    else:
        print("Invalid season entered.")
get_random_temp2(season = input("What is the season? "))
    

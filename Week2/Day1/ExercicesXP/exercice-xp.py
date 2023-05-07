# Exercice 1 : : Hello World
# Print the following output in one line of code: Hello world Hello world Hello world Hello world
print("Hello World "*4)


# Exercice 2 : Some Math
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99**3)*8)


# Exercise 3 : What Is The Output ?
# Predict the output of the following code snippets:
# 5 < 3 -> False
# 3 == 3 -> True
# 3 == "3" -> False
# "3" > 3 -> False
# "Hello" == "hello" -> False


# Exercise 4 : Your Computer Brand
computer_brand = "asus"
print(f"I have an {computer_brand} computer")


# Exercise 5 : Your Information
name = "Michael"
age = 43
shoe_size = 42
info = print(f"My name is {name} and I'm {age}. I love shoes and if you want to make me a gift, my shoe size is {shoe_size}")


# Exercise 6 : A & B
a = 6
b = 3
if a > b:
    print("Hello World")

# Exercise 7 : Odd Or Even
num = int(input ("Enter any number "))
if (num % 2) == 0: 
    print("The number is even") 
else: print("The provided number is odd") 


# Exercise 8 : What’s Your Name ?
name = input("What's your name? ")
if name == "Michael":
    print("Great! You have the best name in the world! ")
else:
    print ("Ugly name! ")


# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("What is your height? "))
height *= 2.54
if height >= 145:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")
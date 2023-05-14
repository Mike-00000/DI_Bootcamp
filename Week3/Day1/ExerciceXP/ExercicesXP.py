
# EXERCICE XP -------------------------------------------------------------------

# Exercise 1: Cats --------------------------------------------------------------
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat("Bob", 2)
# cat2 = Cat("Lili", 5)
# cat3 = Cat("Bobo", 9)

# def oldest_cat(c1, c2, c3):
#     cats = [c1.age, c2.age, c3.age]
#     return max(cats)

# print(f"The oldest cat is {oldest_cat(cat1,cat2,cat3)} years old.")



# Exercise 2 : Dogs ----------------------------------------------------------------
# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height
    
#     def bark(self):
#         print(f"{self.name} said woof woof")
    
#     def jump(self):
#         high_jump = self.height * 2
#         print(f"{self.name} jump {high_jump}cm high!")
#         return(high_jump)

# (Dog("Bob", 50))

# davidsdog = Dog("Rex", 50)
# print(f"David's dog is called {davidsdog.name}, and is {davidsdog.height} cm.")
# davidsdog.bark
# davidsdog.jump

# sarahs_dog = Dog("Teacup", 20)
# print(f"Sarah's dog is called {sarahs_dog.name}, and is {sarahs_dog.height} cm.")
# sarahs_dog.bark
# sarahs_dog.jump

# if davidsdog.height > sarahs_dog.height:
#     print(f"David's dog is bigger. It is {davidsdog.height}cm")
# else:
#     print(f"Sarah's dog is bigger. It is {sarahs_dog.height}cm")


# Exercise 3 : Who’s The Song Producer? --------------------------------------------------
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
        
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(f"{line}")
        

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()



# Exercise 4 : Afternoon At The Zoo -------------------------------------------------------
# class Zoo:
#     def __init__(self, zoo_name):


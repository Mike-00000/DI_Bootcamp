# EXERCICES XP ---------------------------------------------------------
# Exercise 1 : Pets ----------------------------------------------------

# class Pets:
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(f"{animal.name} is walking")

# class Cat(Pets):
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# cat_instance1 = Bengal("Lili", 5)
# cat_instance2 = Chartreux("Lolo", 2)
# cat_instance3 = Siamese("Lulu", 9)

# all_cats = [cat_instance1, cat_instance2, cat_instance3]

# cat_instances = []

# sarapets = Pets(all_cats)
# print(sarapets.walk())




# Exercise 2 : Dogs ----------------------------------------------------

class Dogs:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print(f"{self.name} is barking ")
    
    def run_speed(self):
        rs = self.weight / self.age * 10
        print(f"the dog is running speed {self.weight / self.age *10}")
        return rs
    
    def run_weight(self):
        rw = self.run_speed() * self.weight
        return rw
    
    def fight(self, dog2):
        if self.run_weight() > dog2.run_weight():
            print(f"{self.name} won the fight")
        else:
            print(f"{dog2.name} won the fight")
    
dog1 = Dogs("Bob", 8, 20)
dog2 = Dogs("Lili", 5, 30)
dog3 = Dogs("Bubu", 3, 8)

dog1.run_speed()
dog2.run_speed()
dog3.run_speed()

dog1.run_weight()
dog2.run_weight()
dog3.run_weight()

dog1.fight(dog2)
dog3.fight(dog1)
dog2.fight(dog3)




# 
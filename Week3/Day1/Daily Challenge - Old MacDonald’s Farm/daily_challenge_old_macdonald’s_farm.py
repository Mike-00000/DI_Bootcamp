
# Daily Challenge: Old MacDonald’s Farm ----------------------------------------

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "E-I-E-I-0!"
        return info
    
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_string = ", ".join(animal_types)
        return f"{self.name}'s farm has {animals_string}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
animal_types = macdonald.get_animal_types()
print(animal_types)
short_info = macdonald.get_short_info()
print(short_info)
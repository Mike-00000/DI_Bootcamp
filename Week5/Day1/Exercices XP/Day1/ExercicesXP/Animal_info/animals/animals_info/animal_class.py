import json
import os

class Animal:
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), 'data.json')
    
    def get_all_animals(self):
        with open(self.data_file, 'r') as file:
            data = json.load(file)
        return data['animals']
    
    def get_single_animal(self, animal_id):
        with open(self.data_file, 'r') as file:
            data = json.load(file)
        animals = data['animals']
        for animal in animals:
            if animal['id'] == animal_id:
                return animal
        return None
from django.shortcuts import render, get_object_or_404, redirect
from .models import Family, Animal
from .animal_class import Animal as AnimalClass
import os
import json

def home(request):
    return render(request, 'animals_info/home.html')

def load_data(request):
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return render(request, 'animals_info/load_data.html')

def family_detail(request, family_id):
    animal_obj = Animal()
    family = get_object_or_404(Family, id=family_id)
    animals = animal_obj.get_all_animals()
    family_animals = [animal for animal in animals if animal['family'] == family.name]
    return render(request, 'animals_info/family_detail.html', {'family': family, 'animals': family_animals})


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animals_info/animal_detail.html', {'animal': animal})

def animal_list(request):
    animal_obj = AnimalClass()
    animals = animal_obj.get_all_animals()
    return render(request, 'animals_info/animal_list.html', {'animals': animals})



def animal_redirect(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return redirect('animal_detail', animal_id=animal_id)


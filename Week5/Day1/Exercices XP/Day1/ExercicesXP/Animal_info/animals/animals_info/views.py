from django.shortcuts import render, get_object_or_404
from .models import Family, Animal
import os
import json

def load_data(request):
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
        # Code pour charger les données dans la base de données Django
    return render(request, 'animals_info/load_data.html')

def family_detail(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    animals = Animal.objects.filter(family=family)
    return render(request, 'animals_info/family_detail.html', {'family': family, 'animals': animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animals_info/animal_detail.html', {'animal': animal})


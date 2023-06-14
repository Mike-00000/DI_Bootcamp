from django.shortcuts import render, get_object_or_404, redirect
from .models import Family, Animal
from . import views
import random
import pyttsx3
import pronouncing
from django.http import HttpResponse


def family_detail(request, family_id):
    family = get_object_or_404(Family, pk=family_id)
    animals = Animal.objects.filter(family=family).order_by('name')
    num_animals = animals.count()
    return render(request, 'family_detail.html', {'family': family, 'animals': animals, 'num_animals': num_animals})


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})


def animal_list(request):
    min_speed = 0
    max_speed = 100
    animals = Animal.objects.filter(speed__gte=min_speed, speed__lte=max_speed).order_by('speed')
    return render(request, 'animal_list.html', {'animals': animals})



song_animals = [
    {'name': 'Cat', 'family': 'Mammal'},
    {'name': 'Elephant', 'family': 'Mammal'},
    {'name': 'Giraffe', 'family': 'Mammal'},
    {'name': 'Turtle', 'family': 'Reptile'},
    {'name': 'Snake', 'family': 'Reptile'},
    {'name': 'Butterfly', 'family': 'Insect'},
    {'name': 'Spider', 'family': 'Arachnid'},
    {'name': 'Frog', 'family': 'Amphibian'},
]

def generate_children_song():
    animal = random.choice(song_animals)
    rhyming_words = pronouncing.rhymes(animal['name'].lower())
    if rhyming_words:
        rhyming_word = random.choice(rhyming_words)
    else:
        rhyming_word = animal['name']
    
    song = f"In the animal kingdom, we have a {animal['name']}, a {animal['family'].lower()}."
    song += f" It's the {rhyming_word} from the {animal['family'].lower()}."
    
    return song

def children_song(request):
    children_song = generate_children_song()

    engine = pyttsx3.init()
    engine.say(children_song)
    engine.runAndWait()

    return HttpResponse()
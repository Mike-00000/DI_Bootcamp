from django.shortcuts import render, get_object_or_404
from .models import Family, Animal
from . import views


# Create your views here.
def family_detail(request, family_id):
    family = get_object_or_404(Family, pk=family_id)
    animals = Animal.objects.filter(family=family)
    return render(request, 'family_detail.html', {'family': family, 'animals': animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})


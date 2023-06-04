from django.shortcuts import render
from .models import Person

# Create your views here.

def people_list(request):
    people = Person.objects.order_by('age')
    return render(request, 'people_list.html', {'people': people})

def person_detail(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'person_detail.html', {'person': person})


from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def search_by_phonenumber(request):
    if request.method == 'GET':
        phonenumber = request.GET.get('phonenumber', '')
        try:
            person = Person.objects.get(phone_number=phonenumber)
            context = {'person': person}
            return render(request, 'person_phonenumber.html', context)
        except Person.DoesNotExist:
            message = f"No person found with phone number: {phonenumber}"
            return render(request, 'person_phonenumber.html', {'message': message})
    return HttpResponse("Invalid request method")


def search_by_name(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        try:
            person = Person.objects.get(name__iexact=name)
            context = {'person': person}
            return render(request, 'person_name.html', context)
        except Person.DoesNotExist:
            message = f"No person found with name: {name}"
            return render(request, 'person_name.html', {'message': message})
    return HttpResponse("Invalid request method")


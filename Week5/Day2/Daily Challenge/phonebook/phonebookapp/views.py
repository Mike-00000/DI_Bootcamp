from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, PersonSearchForm

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


def search_person(request):
    if request.method == 'POST':
        form = PersonSearchForm(request.POST)
        if form.is_valid():
            search_value = form.cleaned_data['search']
            if search_value.isdigit():
                # Redirect to search by phone number view
                return redirect('search_by_phonenumber', phonenumber=search_value)
            else:
                # Redirect to search by name view
                return redirect('search_by_name', name=search_value)
    else:
        form = PersonSearchForm()
    
    return render(request, 'search_person.html', {'form': form})


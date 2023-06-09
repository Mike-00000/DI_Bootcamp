from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'visitors/home.html'

def hotel_info(request):
    # Votre code pour afficher les informations de l'hôtel ici
    return render(request, 'visitors/hotel_info.html')

def room_availability(request):
    # Your code to check room availability and display it
    return render(request, 'visitors/room_availability.html')


def information_page(request):
    return render(request, 'visitors/information_page.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the appropriate URL name
        else:
            # Handle invalid login credentials
            return render(request, 'visitors/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'visitors/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the appropriate URL name
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Gif, Category
from .forms import GifForm, CategoryForm
import requests

def index(request):
    gifs = Gif.objects.all()
    return render(request, 'index.html', {'gifs': gifs})


def new_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GifForm()
    return render(request, 'new_gif.html', {'form': form})


def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CategoryForm()
    return render(request, 'new_category.html', {'form': form})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    gifs = Gif.objects.filter(categories=category)
    return render(request, 'category.html', {'category': category, 'gifs': gifs})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def gif(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    return render(request, 'gif.html', {'gif': gif})




def populate_gifs_from_giphy():
    url = 'https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        gifs = data['data'][:100]  # Récupère les 100 premiers GIFs
        
        for gif in gifs:
            # Récupère les informations du GIF à partir de la réponse JSON
            title = gif['title']
            url = gif['images']['original']['url']
            uploader_name = gif['username']
            
            # Crée un nouvel objet Gif dans la base de données avec les informations récupérées
            new_gif = Gif(title=title, url=url, uploader_name=uploader_name)
            new_gif.save()
            
        print('GIFs ajoutés à la base de données.')
    else:
        print('Une erreur s\'est produite lors de la récupération des GIFs depuis Giphy.')

def my_view(request):
    # Ton code existant pour cette vue
    
    # Appelle la fonction pour ajouter les GIFs à la base de données
    populate_gifs_from_giphy()
    
    # Le reste de ton code pour la vue
    
    return render(request, 'my_template.html', context)

def populate_gifs_view(request):
    # Logique pour créer les GIFs à partir de l'API Giphy
    # Utilise la fonction populate_gifs_from_giphy() ici
    populate_gifs_from_giphy()
    return render(request, 'populate_gifs.html')


def popular_gifs(request):
    popular_gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    return render(request, 'popular_gifs.html', {'popular_gifs': popular_gifs})

def increment_like(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes += 1
    gif.save()
    return redirect('gif', gif_id=gif.id)

def decrement_like(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes -= 1
    gif.save()
    return redirect('gif', gif_id=gif.id)


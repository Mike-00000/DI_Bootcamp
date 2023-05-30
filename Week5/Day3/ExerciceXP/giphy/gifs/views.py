from django.shortcuts import render

from django.http import HttpResponseRedirect
from .models import Gif, Category
from .forms import GifForm, CategoryForm


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

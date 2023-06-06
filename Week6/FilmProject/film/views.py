from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from django.views.generic.edit import UpdateView
from .models import Film, Director
from django import forms
from django.views.generic import TemplateView, DeleteView
from .forms import SearchForm, FilmForm, DirectorForm, AddPosterForm, AddPosterFilmForm, AddFilmForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View, generic



# Create your views here.

class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Film

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            films_all = Film.objects.filter(title__icontains=query)
        else:
            films_all = Film.objects.all()

        return films_all
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        context['search'] = search_form

        context['films'] = self.get_queryset()

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        context['search_form'] = search_form
        return context

class FilmCreateView(CreateView):
    model = Film
    form_class = AddFilmForm
    template_name = 'film/add_film.html'
    success_url = '/films/homepage/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poster_form'] = AddPosterForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        poster_form = context['poster_form']
        if poster_form.is_valid():
            poster = poster_form.save(commit=False)
            poster.film = form.save()
            poster.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'film/director_form.html'  # Replace with your desired template path
    success_url = '/directors/'  # Replace with your desired success URL

class FilmUpdateView(UserPassesTestMixin, UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/film_form.html'  # Replace with your desired template path
    success_url = '/films/homepage/'  # Replace with your desired success URL

    def test_func(self):
        return self.request.user.is_superuser


class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = 'film/director_form.html'  # Replace with your desired template path
    success_url = '/films/homepage/'  # Replace with your desired success URL

    def test_func(self):
        return self.request.user.is_superuser
    
def add_poster(request):
    if request.method == 'POST':
        form = AddPosterForm(request.POST, request.FILES)
        if form.is_valid():
            poster = form.save()  # Save the form data and create a new Poster object
            # Associate the poster with the film (e.g., by setting the foreign key relationship)
            film = ...  # Get the corresponding Film object
            film.poster = poster
            film.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = AddPosterForm()
    
    return render(request, 'add_poster.html', {'form': form})

def FilmCreateView(request):
    if request.method == 'POST':
        form = AddPosterFilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Faire quelque chose après la création du film
            return redirect('homepage')
    else:
        form = AddPosterFilmForm()
    
    return render(request, 'film/create.html', {'form': form})


class FilmDeleteView(UserPassesTestMixin, DeleteView):
    model = Film
    template_name = 'film/confirm_delete.html'
    success_url = reverse_lazy('homepage')

    def test_func(self):
        return self.request.user.is_superuser
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Film deleted successfully.')
        return super().delete(request, *args, **kwargs)
    
class FavouriteFilmView(View):
    def get(self, request, film_id):
        film = Film.objects.get(id=film_id)
        user = request.user  # Use the default User model
        if user.is_authenticated:
            if film.favorite_users.filter(id=user.id).exists():
                film.favorite_users.remove(user)
            else:
                film.favorite_users.add(user)
            return HttpResponse('Success')
        else:
            return HttpResponse('Unauthorized', status=401)
        
class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'film/filmDetail.html'

    
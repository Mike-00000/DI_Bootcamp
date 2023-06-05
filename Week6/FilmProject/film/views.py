from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import Film, Director
from django import forms
from django.views.generic import TemplateView
from .forms import SearchForm, FilmForm, DirectorForm

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
    form_class = FilmForm
    template_name = 'film/film_form.html'  # Replace with your desired template path
    success_url = '/films/'  # Replace with your desired success URL

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'film/director_form.html'  # Replace with your desired template path
    success_url = '/directors/'  # Replace with your desired success URL

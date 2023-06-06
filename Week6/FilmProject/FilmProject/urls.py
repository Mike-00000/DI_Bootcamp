"""
URL configuration for FilmProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from film.views import HomePageView, AboutPageView, FilmCreateView, DirectorCreateView, FilmUpdateView, DirectorUpdateView, FilmDeleteView
from django.contrib.auth import views as auth_views
from film.views import FavouriteFilmView, FilmDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/homepage/', HomePageView.as_view(), name='homepage'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('films/addFilm/', FilmCreateView, name='add_film'),
    path('films/editFilm/<int:pk>/', FilmUpdateView.as_view(), name='edit_film'),
    path('films/addDirector/', DirectorCreateView.as_view(), name='add_director'),
    path('films/editDirector/<int:pk>/', DirectorUpdateView.as_view(), name='edit_director'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path('films/deleteFilm/<int:pk>/', FilmDeleteView.as_view(), name='delete_film'),
    path('films/favouriteFilm/<int:film_id>/', FavouriteFilmView.as_view(), name='favourite_film'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
]


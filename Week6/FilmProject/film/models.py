from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=timezone.now)
    created_in_country = models.ForeignKey(
        'Country',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='films_created',
        default=1
    )
    available_in_countries = models.ManyToManyField('Country', related_name='available_films')
    category = models.ManyToManyField('Category')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    favorite_users = models.ManyToManyField(User, related_name='favorite_films', blank=True)

    def __str__(self):
        return self.title


class Poster(models.Model):
    film = models.OneToOneField(Film, on_delete=models.CASCADE, related_name='poster')
    image = models.ImageField(upload_to='posters/')
    explanation_img = models.CharField(max_length=100)

    def __str__(self):
        return f"Poster for {self.film.title}"


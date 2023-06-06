# Generated by Django 4.2.1 on 2023-06-06 18:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('film', '0007_remove_film_director_poster_film_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='favorite_users',
            field=models.ManyToManyField(blank=True, related_name='favorite_films', to=settings.AUTH_USER_MODEL),
        ),
    ]

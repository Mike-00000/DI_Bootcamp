# Generated by Django 4.2.1 on 2023-06-06 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0006_remove_film_director_film_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posters/')),
                ('explanation_img', models.CharField(max_length=100)),
                ('film', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='film.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='film.director'),
        ),
    ]

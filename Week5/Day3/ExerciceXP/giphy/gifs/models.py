from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField('Gif')

    def __str__(self):
        return self.name

class Gif(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    uploader_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

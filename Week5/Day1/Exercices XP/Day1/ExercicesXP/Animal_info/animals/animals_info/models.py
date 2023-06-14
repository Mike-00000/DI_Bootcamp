from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100, default='Default Name')
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/animal_images', default='default.jpg')

    def __str__(self):
        return self.name


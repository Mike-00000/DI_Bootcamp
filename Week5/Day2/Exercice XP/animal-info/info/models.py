from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100, default='')
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='animals/images', blank=True, null=True)

    def __str__(self):
        return self.name

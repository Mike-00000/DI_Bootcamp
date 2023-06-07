from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'phonebookapp'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'phonebookapp'

class Email(models.Model):
    email_address = models.EmailField()

    def __str__(self):
        return self.email_address

    class Meta:
        app_label = 'phonebookapp'

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"

    class Meta:
        app_label = 'phonebookapp'



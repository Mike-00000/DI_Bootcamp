from django.contrib import admin
from .models import Person, Category, Post, Email, Address
# Register your models here.
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Email)
admin.site.register(Address)
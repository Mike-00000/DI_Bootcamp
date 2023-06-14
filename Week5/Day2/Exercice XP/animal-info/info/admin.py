from django.contrib import admin
from .models import Family, Animal

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

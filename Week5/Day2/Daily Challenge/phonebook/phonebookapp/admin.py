from django.contrib import admin
from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, RegionalPhoneNumberWidget
from .models import Person, Post, Category, Email, Address
from .forms import PersonForm

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    list_display = ('name', 'email', 'phone_number', 'address')
    list_display_links = ('name', 'email', 'address')
    search_fields = ('name', 'email', 'phone_number', 'address')
    exclude = ('id',)

    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget},
    }

admin.site.register(Person, PersonAdmin)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Email)
admin.site.register(Address)


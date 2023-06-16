from django.contrib import admin
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from .models import Person, Post, Category, Email, Address, PersonAdmin
# Register your models here.


class PersonForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget)

    class Meta:
        model = Person
        fields = '__all__'

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    list_display = ('name', 'email', 'address')
    list_display_links = ('name', 'email', 'address')
    search_fields = ('name', 'email', 'phone_number')
    exclude = ('id',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Email)
admin.site.register(Address)


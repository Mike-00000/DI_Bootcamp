from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from .models import Person



class PersonSearchForm(forms.Form):
    search = forms.CharField(label='Search')

class PersonForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget)

    class Meta:
        model = Person
        fields = '__all__'

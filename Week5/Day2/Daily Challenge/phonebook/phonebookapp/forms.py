from django import forms

class PersonSearchForm(forms.Form):
    search = forms.CharField(label='Search')

from django import forms
from film.models import Film, Director

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'  # Include all fields from the Film model

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'  # Include all fields from the Director model

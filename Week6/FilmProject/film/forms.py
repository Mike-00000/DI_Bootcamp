from django import forms
from film.models import Film, Director, Poster

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'  # Include all fields from the Film model

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'  # Include all fields from the Film model

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'  # Include all fields from the Director model

class AddPosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['image', 'explanation_img']

class AddPosterFilmForm(forms.Form):
    film_form = FilmForm()
    poster_form = AddPosterForm()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(self.film_form.fields)
        self.fields.update(self.poster_form.fields)

    def save(self):
        film = self.film_form.save()
        poster = self.poster_form.save(commit=False)
        poster.film = film
        poster.save()

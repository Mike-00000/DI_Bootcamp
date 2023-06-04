from django import forms
from .models import Category, Post

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ('author')
        widgets = {
            'author': forms.HiddenInput(),
            'content': forms. Textarea(attrs={'rows': 3, 'class': 'content_class'})
        }
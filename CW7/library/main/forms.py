from django import forms
from .models import book

class LibraryModelForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['title', 'author']
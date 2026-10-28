from django import forms
from .models import Movies
class dataform(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        
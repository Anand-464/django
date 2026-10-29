from django import forms
from .models import Weight_enter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight_enter
        fields = ['weight']
        labels = {
            'weight': 'Weight in kilograms',
        }



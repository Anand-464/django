from django import forms
from .models import Weight_enter


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight_enter
        fields = ['weight']
        labels = {
            'weight': 'Weight in kilograms',
        }



from django import forms
class Entermovie(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    year = forms.CharField(widget=forms.NumberInput)
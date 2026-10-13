from django import forms
class dataform(forms.Form):
    name = forms.CharField()
    year = forms.CharField()
    genre = forms.CharField()
    rating = forms.CharField()
 
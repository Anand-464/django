from django import forms
class Contact(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    phonenumber = forms.CharField(widget=forms.NumberInput)
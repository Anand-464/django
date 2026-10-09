from django import forms
class LoginForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    age = forms.CharField()
    address = forms.CharField()
 
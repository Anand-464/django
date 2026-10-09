from django import forms
from django.core.validators import validate_email
class LoginForm(forms.Form):
    email = forms.CharField(validators=[validate_email])
    name = forms.CharField(max_length=50, min_length= 5)
    password = forms.CharField(max_length= 20,min_length= 8)
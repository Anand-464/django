from django import forms
from .models import User_Profile
class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'first_name',
        'last_name',
        'subject',
        'years_of_experience',
        'profile_photo'
        ]
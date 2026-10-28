from django import forms
from .models import Stu_Profile
class Profile_Form(forms.ModelForm):
    class Meta:
        model = Stu_Profile
        fields = [
        'fname',
        'course',
        'phonenum',
        'email',
        'id_proof'
        ]
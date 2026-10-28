from django.db import models

class User_Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length = 200)
    subject = models.CharField(max_length=500)
    years_of_experience = models.DecimalField(max_digits=2, decimal_places=1)
    profile_photo = models.FileField()
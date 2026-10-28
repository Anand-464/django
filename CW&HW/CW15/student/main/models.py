from django.db import models

class Stu_Profile(models.Model):
    fname = models.CharField(max_length=200)
    course = models.CharField(max_length = 200)
    phonenum = models.CharField(max_length=10)
    email = models.EmailField(default = None)
    id_proof = models.FileField()

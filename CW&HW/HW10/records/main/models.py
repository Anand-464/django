from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    stu_class = models.CharField(max_length=50)
    age = models.IntegerField()


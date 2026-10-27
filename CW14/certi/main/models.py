from django.db import models

class Certificate(models.Model):
    student_name = models.CharField(max_length=150)
    student_email = models.EmailField()
    course_name = models.CharField(max_length=200)
    completion_date = models.DateField()

